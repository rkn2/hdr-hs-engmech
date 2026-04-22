"""
Generates Chapter_12.ipynb — Counting Principles (Structural Engineering version)
Grounded in Hibbeler Chapter 1 (ASCE load combinations) and Chapter 3 (truss member arrangements)
"""
import json, os
from itertools import combinations

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

CELLS = [
cell("markdown","title",[
"# Chapter 12: Counting Principles in Structural Engineering\n",
"## How Many Ways Can a Structure Be Loaded?\n",
"\n",
"**Learning Objectives:**\n",
"- Apply the multiplication rule for counting to structural load combinations\n",
"- Use combinations to count truss member arrangements and inspection schedules\n",
"- Explain why engineers must check *every* load combination — and what happens when one is missed\n",
]),

cell("markdown","photo",[
"<center>\n",
"<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Hartford_Civic_Center_Coliseum.jpg/800px-Hartford_Civic_Center_Coliseum.jpg' width='650' />\n",
"\n",
"<em>The Hartford Civic Center, Hartford, Connecticut. The roof of the arena collapsed "
"in January 1978 under accumulated snow and dead load — eighteen hours after 5,000 fans left a basketball game. "
"(Wikimedia Commons — CC BY-SA.)</em>\n",
"</center>\n",
"\n",
"---\n",
]),

cell("code","setup",[
"import subprocess, sys\n",
"subprocess.run([sys.executable,'-m','pip','install','ipywidgets','--quiet'])\n",
"import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"import matplotlib.patches as mpatches\n",
"import ipywidgets as widgets\n",
"from IPython.display import display\n",
"from itertools import combinations as combs\n",
"import math\n",
"%matplotlib inline\n",
"print('Libraries loaded.')\n",
]),

cell("markdown","why",[
"## 12.1  The Multiplication Rule in Structural Design\n",
"\n",
"When an engineer designs a structure, they must ask: *what combinations of loads could act on this structure at the same time?*\n",
"\n",
"Hibbeler §1.3 identifies the primary load types a structure must resist. The ASCE/SEI 7-10 standard — referenced throughout Chapter 1 — specifies that structural members must be designed to resist the most demanding of **seven basic load combinations**. Each combination multiplies the individual loads by *load factors* that account for uncertainty:\n",
"\n",
"| Combination | Formula |\n",
"|-------------|--------|\n",
"| 1 | 1.4D |\n",
"| 2 | 1.2D + 1.6L + 0.5(Lr or S or R) |\n",
"| 3 | 1.2D + 1.6(Lr or S or R) + (L or 0.5W) |\n",
"| 4 | 1.2D + 1.0W + L + 0.5(Lr or S or R) |\n",
"| 5 | 0.9D + 1.0W |\n",
"| 6 | 1.2D + 1.0E + L + 0.2S |\n",
"| 7 | 0.9D + 1.0E |\n",
"\n",
"Where **D** = dead, **L** = live, **Lr** = roof live, **S** = snow, **R** = rain, **W** = wind, **E** = earthquake.\n",
"\n",
"**Why seven combinations?** Because each load type has a different probability of being at its maximum simultaneously with other loads. The multiplication rule for counting tells us the *maximum possible* number of combinations — and the code's job is to select which ones actually govern design.\n",
]),

cell("markdown","exp1intro",[
"## 🔬 Interactive Experiment 1: Building Your Own Load Combination\n",
"\n",
"Use the checkboxes below to select which load types are present at your site (e.g., a building in a snowy, windy region near a fault line has all of them). The widget shows which ASCE 7-10 combinations apply and what the total factored load looks like.\n",
]),

cell("code","widget1",[
"LOAD_FACTORS = {\n",
"    'Dead (D)':         {'D':1.2, 'combo':'Standard'},\n",
"    'Live (L)':         {'L':1.6, 'combo':'Occupancy'},\n",
"    'Roof Live (Lr)':   {'Lr':1.6,'combo':'Roof'},\n",
"    'Snow (S)':         {'S':1.6, 'combo':'Roof'},\n",
"    'Wind (W)':         {'W':1.0, 'combo':'Lateral'},\n",
"    'Earthquake (E)':   {'E':1.0, 'combo':'Seismic'},\n",
"    'Rain (R)':         {'R':1.6, 'combo':'Roof'},\n",
"}\n",
"\n",
"# Representative nominal loads (kips) — loosely based on the two-story office building\n",
"# discussed in Hibbeler §1.2-1.3 context (dead load from floor/roof system,\n",
"# live load from ASCE 7-10 Table 4-1 office occupancy). Values are illustrative;\n",
"# Hibbeler does not tabulate a single canonical example with all seven load types.\n",
"NOMINAL = {'D':40, 'L':20, 'Lr':10, 'S':15, 'W':12, 'E':18, 'R':8}\n",
"\n",
"COMBINATIONS = [\n",
"    ('1',  lambda s: 1.4*s.get('D',0)),\n",
"    ('2',  lambda s: 1.2*s.get('D',0)+1.6*s.get('L',0)+0.5*max(s.get('Lr',0),s.get('S',0),s.get('R',0))),\n",
"    ('3',  lambda s: 1.2*s.get('D',0)+1.6*max(s.get('Lr',0),s.get('S',0),s.get('R',0))+max(s.get('L',0),0.5*s.get('W',0))),\n",
"    ('4',  lambda s: 1.2*s.get('D',0)+1.0*s.get('W',0)+s.get('L',0)+0.5*max(s.get('Lr',0),s.get('S',0),s.get('R',0))),\n",
"    ('5',  lambda s: 0.9*s.get('D',0)+1.0*s.get('W',0)),\n",
"    ('6',  lambda s: 1.2*s.get('D',0)+1.0*s.get('E',0)+s.get('L',0)+0.2*s.get('S',0)),\n",
"    ('7',  lambda s: 0.9*s.get('D',0)+1.0*s.get('E',0)),\n",
"]\n",
"\n",
"checks = {k: widgets.Checkbox(value=(k in ['Dead (D)','Live (L)']), description=k,\n",
"    layout=widgets.Layout(width='200px')) for k in LOAD_FACTORS}\n",
"\n",
"def _combo_plot(**kwargs):\n",
"    selected = {k.split(' ')[0].rstrip('(').lstrip(): NOMINAL[k.split('(')[1].rstrip(')')] \n",
"                for k,v in kwargs.items() if v}\n",
"    combos_vals = [(name, fn(selected)) for name, fn in COMBINATIONS]\n",
"    names = [f'Combo {c[0]}' for c in combos_vals]\n",
"    vals  = [c[1] for c in combos_vals]\n",
"    governing_idx = int(np.argmax(vals))\n",
"\n",
"    fig, ax = plt.subplots(figsize=(10, 5))\n",
"    colors = ['firebrick' if i == governing_idx else 'steelblue' for i in range(len(vals))]\n",
"    bars = ax.bar(names, vals, color=colors, edgecolor='white', width=0.6)\n",
"    ax.set_ylabel('Factored Load (kips)', fontsize=12)\n",
"    ax.set_title('ASCE 7-10 Load Combinations — Which Governs?', fontsize=13)\n",
"    for bar, val in zip(bars, vals):\n",
"        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f'{val:.0f}',\n",
"            ha='center', fontsize=10)\n",
"    ax.annotate(f'Governing: Combo {combos_vals[governing_idx][0]}  ({vals[governing_idx]:.0f} kips)',\n",
"        xy=(0.5, 0.93), xycoords='axes fraction', ha='center', fontsize=11,\n",
"        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.9))\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"box_grid = widgets.GridBox(list(checks.values()), layout=widgets.Layout(grid_template_columns='repeat(3,210px)'))\n",
"out1 = widgets.interactive_output(_combo_plot, {k: v for k,v in checks.items()})\n",
"display(widgets.VBox([box_grid, out1]))\n",
]),

cell("markdown","casestudy",[
"---\n",
"## ⚠️  Real-World Case: The Hartford Civic Center Roof Collapse (1978)\n",
"\n",
"On January 18, 1978 — just 18 hours after 5,000 fans left a University of Connecticut basketball game — the roof of the Hartford Civic Center collapsed. No one was killed. The structure had been open for less than three years.\n",
"\n",
"**What went wrong:**\n",
"\n",
"The roof was a two-way space frame: a three-dimensional truss system spanning 300 ft × 360 ft with no interior columns. The design engineers used a computer analysis program — cutting-edge for 1973 — to check the structure.\n",
"\n",
"The investigation found three compounding failures, all rooted in counting:\n",
"\n",
"1. **The dead load was underestimated** — the computer model used a self-weight that was 20% lower than the structure as actually built. Electrical equipment and mechanical systems added to the roof were never added to the load model.\n",
"\n",
"2. **The critical load combination was never checked** — the governing case of dead load + snow load + ponded water (from melting and refreezing) produced a load far exceeding the design capacity. This combination existed in the ASCE standards but was not checked in the computer run.\n",
"\n",
"3. **The slender compression members buckled** — the top chord members of the space frame were slender enough that they were governed by buckling (Euler's formula, which Hibbeler covers in later chapters), not direct compression strength. The analysis used the wrong failure mode.\n",
"\n",
"The roof had been deflecting visibly for months — workers had placed buckets to catch leaks from the sagging panels. No one connected the dots.\n",
"\n",
"> *The multiplication rule of counting works in both directions: the number of combinations you must check is large. Missing even one can be fatal.*\n",
]),

cell("markdown","exp2intro",[
"## 🔬 Interactive Experiment 2: How Many Ways Can You Inspect a Truss?\n",
"\n",
"A simple Pratt truss bridge has many individual members. An inspector has time to thoroughly check only a subset of them on a given visit. The combination formula C(n, k) = n! / (k! × (n-k)!) tells us how many different inspection subsets are possible.\n",
"\n",
"Use the sliders to explore how the number of possible inspection schedules grows — and why a *systematic* sampling strategy matters more than a random one when resources are limited.\n",
]),

cell("code","widget2",[
"def _truss_combos(n_members, k_inspected):\n",
"    if k_inspected > n_members:\n",
"        k_inspected = n_members\n",
"    n_combos = math.comb(n_members, k_inspected)\n",
"    pct = k_inspected / n_members * 100\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    # Left: bar of inspected vs not\n",
"    ax1.bar(['Inspected', 'Not Inspected'], [k_inspected, n_members - k_inspected],\n",
"        color=['steelblue', 'lightgray'], edgecolor='white', width=0.5)\n",
"    ax1.set_ylabel('Number of Members', fontsize=12)\n",
"    ax1.set_title(f'Truss Inspection Coverage  ({pct:.0f}%)', fontsize=13)\n",
"    ax1.annotate(f'{k_inspected} of {n_members} members\\ninspected this visit',\n",
"        xy=(0.5, 0.85), xycoords='axes fraction', ha='center', fontsize=11,\n",
"        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))\n",
"\n",
"    # Right: how combos grow with k\n",
"    ks = list(range(1, n_members+1))\n",
"    cs = [math.comb(n_members, k) for k in ks]\n",
"    ax2.bar(ks, cs, color=['firebrick' if k == k_inspected else 'steelblue' for k in ks],\n",
"        edgecolor='white')\n",
"    ax2.set_xlabel('Members Inspected (k)', fontsize=12)\n",
"    ax2.set_ylabel('Possible Inspection Schedules  C(n,k)', fontsize=12)\n",
"    ax2.set_title(f'C({n_members}, k) — Number of Ways to Choose k Members', fontsize=13)\n",
"    ax2.annotate(f'C({n_members},{k_inspected}) = {n_combos:,}',\n",
"        xy=(0.55, 0.85), xycoords='axes fraction', fontsize=11,\n",
"        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.9))\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"w_n = widgets.IntSlider(value=12, min=5, max=30, step=1,\n",
"    description='Truss members (n):', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='400px'))\n",
"w_k = widgets.IntSlider(value=4, min=1, max=20, step=1,\n",
"    description='Members inspected (k):', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='400px'))\n",
"out2 = widgets.interactive_output(_truss_combos, {'n_members': w_n, 'k_inspected': w_k})\n",
"display(widgets.VBox([w_n, w_k, out2]))\n",
]),

cell("markdown","review",[
"---\n",
"## 📋  Chapter 12 Review\n",
"\n",
"| Concept | Structural Application |\n",
"|---------|----------------------|\n",
"| **Multiplication rule** | Number of ways k load types can combine = product of individual options |\n",
"| **Combinations C(n,k)** | Ways to select k members for inspection from n total; ways to select k load types from n available |\n",
"| **Permutations** | Order-sensitive counting — e.g., the sequence in which loads are applied during a proof load test |\n",
"| **Factorial n!** | Number of ways to order n inspection events |\n",
"\n",
"**The Big Idea:** Counting tells engineers how large a problem space they are searching. The ASCE 7-10 load combinations are not arbitrary — they represent the code committee's answer to the combinatorics question: *which subsets of loads can plausibly occur simultaneously, and which combinations produce the worst demands?* When engineers skip combinations, they are not saving time. They are leaving part of the problem unchecked.\n",
]),
]

def build_notebook():
    nb = {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name":"Python 3","language":"python","name":"python3"},
            "language_info": {"name":"python","version":"3.8.0"},
            "colab": {"provenance":[]},
        },
        "cells": CELLS,
    }
    out = os.path.join(os.path.dirname(__file__), '..', 'Chapter_12.ipynb')
    with open(out, 'w') as f: json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == '__main__': build_notebook()
