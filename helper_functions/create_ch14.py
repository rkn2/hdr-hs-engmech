"""
Generates Chapter_14.ipynb — Probability Rules (Structural Engineering version)
Grounded in Hibbeler Chapter 3 (trusses) and structural redundancy / progressive collapse
"""
import json, os

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

CELLS = [
cell("markdown","title",[
"# Chapter 14: Probability Rules in Structural Engineering\n",
"## Series Systems, Parallel Systems, and Progressive Collapse\n",
"\n",
"**Learning Objectives:**\n",
"- Apply the addition rule (OR) and multiplication rule (AND) to structural systems\n",
"- Distinguish series systems from parallel systems and calculate their failure probabilities\n",
"- Define conditional probability and connect it to progressive collapse in structures\n",
"- Explain why redundancy is not just convenient — it is a probabilistic safety strategy\n",
]),

cell("markdown","photo",[
"<center>\n",
"<img src='https://upload.wikimedia.org/wikipedia/commons/4/4f/Oklahoma_City_Bombing_FEMA.jpg' width='700' />\n",
"\n",
"<em>The Alfred P. Murrah Federal Building, Oklahoma City, after the April 19, 1995 bombing. "
"The destruction of front-face columns triggered a progressive collapse that killed 168 people "
"and fundamentally changed how US codes address structural robustness. "
"(FEMA — public domain.)</em>\n",
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
"from matplotlib.patches import FancyArrowPatch\n",
"import ipywidgets as widgets\n",
"from IPython.display import display\n",
"%matplotlib inline\n",
"print('Setup complete.')\n",
]),

cell("markdown","why",[
"## 14.1  Structural Systems as Probability Problems\n",
"\n",
"A structure is not a single element — it is a *system* of interconnected members. Whether the whole system survives depends on which members can fail, how they are connected, and whether the remaining members can redistribute the load.\n",
"\n",
"This maps directly onto probability rules you already know:\n",
"\n",
"### Series System (the chain)\n",
"A **series system** fails if *any one* member fails — like a chain that breaks at its weakest link. Trusses with no redundancy are series systems.\n",
"\n",
"$$P(\\text{system fails}) = 1 - \\prod_{i} (1 - p_i)$$\n",
"\n",
"This uses the **multiplication rule for independent events** (AND): the system *survives* only if member 1 AND member 2 AND ... all survive.\n",
"\n",
"### Parallel System (the team)\n",
"A **parallel system** fails only if *all* members fail — like a team where even one person succeeding is enough. Redundant frames and cable-stayed bridges are parallel systems.\n",
"\n",
"$$P(\\text{system fails}) = \\prod_{i} p_i$$\n",
"\n",
"This uses the **multiplication rule**: the system fails only if member 1 AND member 2 AND ... all fail.\n",
"\n",
"> **Hibbeler connection:** Chapter 3 covers statically determinate trusses — these are series systems. Any single member failure causes the truss to become a mechanism (it collapses). Chapter 10 covers statically indeterminate structures, which are parallel systems — they have redundant load paths.\n",
]),

cell("markdown","exp1intro",[
"## 🔬 Interactive Experiment 1: Series vs. Parallel System Reliability\n",
"\n",
"Use the sliders to set the failure probability of each individual member and the number of members. Compare how the overall system failure probability changes between series (no redundancy) and parallel (full redundancy) configurations.\n",
]),

cell("code","widget1",[
"def _reliability_plot(p_member, n_members):\n",
"    p = p_member / 1000  # slider is in 0.1% units for readability\n",
"    ns = list(range(1, n_members+1))\n",
"\n",
"    p_series   = [1 - (1-p)**k for k in ns]\n",
"    p_parallel = [p**k for k in ns]\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    ax1.plot(ns, [v*100 for v in p_series], 'firebrick', lw=2.5, marker='o', ms=5, label='Series (ANY fails → system fails)')\n",
"    ax1.plot(ns, [v*100 for v in p_parallel], 'steelblue', lw=2.5, marker='s', ms=5, label='Parallel (ALL must fail → system fails)')\n",
"    ax1.set_xlabel('Number of Members', fontsize=12)\n",
"    ax1.set_ylabel('System Failure Probability (%)', fontsize=12)\n",
"    ax1.set_title(f'Series vs. Parallel  (p per member = {p*100:.2f}%)', fontsize=13)\n",
"    ax1.legend(fontsize=10)\n",
"    ax1.set_ylim(-2, 102)\n",
"\n",
"    # Right: diagram showing current n_members value\n",
"    p_s = p_series[n_members-1]\n",
"    p_p = p_parallel[n_members-1]\n",
"    bars = ax2.bar(['Series\\n(Determinate Truss)', 'Parallel\\n(Redundant Frame)'],\n",
"        [p_s*100, p_p*100], color=['firebrick','steelblue'], edgecolor='white', width=0.5)\n",
"    for bar, val in zip(bars, [p_s, p_p]):\n",
"        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,\n",
"            f'{val*100:.4f}%', ha='center', fontsize=11)\n",
"    ax2.set_ylabel('System Failure Probability (%)', fontsize=12)\n",
"    ax2.set_title(f'System Failure at n = {n_members} Members', fontsize=13)\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"    ratio = p_s / p_p if p_p > 0 else float('inf')\n",
"    print(f'Series system:   {p_s*100:.4f}% failure probability')\n",
"    print(f'Parallel system: {p_p*100:.6f}% failure probability')\n",
"    if ratio < 1e9:\n",
"        print(f'The series system is {ratio:.0f}× MORE likely to fail than the parallel system.')\n",
"\n",
"w_p = widgets.IntSlider(value=5, min=1, max=100, step=1,\n",
"    description='P(member fails) × 1000:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"w_n = widgets.IntSlider(value=8, min=2, max=20, step=1,\n",
"    description='Number of members:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"out1 = widgets.interactive_output(_reliability_plot, {'p_member': w_p, 'n_members': w_n})\n",
"display(widgets.VBox([w_p, w_n, out1]))\n",
]),

cell("markdown","conditional",[
"---\n",
"## 14.2  Conditional Probability and Progressive Collapse\n",
"\n",
"**Conditional probability** is the probability of an event given that another event has already occurred:\n",
"\n",
"$$P(B \\mid A) = \\frac{P(A \\text{ and } B)}{P(A)}$$\n",
"\n",
"In structural engineering, this appears in **progressive collapse** — the phenomenon where one member failing increases the probability that neighboring members fail, because they must now carry additional redistributed load.\n",
"\n",
"- $P(\\text{member 2 fails})$ might be 0.1% under normal conditions\n",
"- $P(\\text{member 2 fails} \\mid \\text{member 1 has already failed})$ might be 15% — because the load that member 1 was carrying has now been transferred to member 2\n",
"\n",
"These are **not independent events**. The failure of one member changes the probability of the next.\n",
]),

cell("markdown","casestudy",[
"---\n",
"## ⚠️  Real-World Case: The Alfred P. Murrah Federal Building (Oklahoma City, 1995)\n",
"\n",
"On April 19, 1995, a truck bomb detonated outside the Alfred P. Murrah Federal Building in "
"Oklahoma City, destroying three ground-floor columns on the north face. Within seconds, a "
"progressive collapse had killed 168 people — at the time, the deadliest domestic terrorist attack "
"in US history.\n",
"\n",
"**Why did losing three columns kill 168 people?**\n",
"\n",
"The Murrah Building used widely spaced ground-floor columns with a massive **transfer girder** "
"above that carried upper-floor loads and redistributed them to the columns below. "
"When the blast destroyed the front columns, the transfer girder lost its support and failed. "
"This triggered a conditional probability chain:\n",
"\n",
"$$P(\\\\text{floor fails} \\\\mid \\\\text{transfer girder has failed}) \\\\approx 1.0$$\n",
"\n",
"Without the transfer girder, the floors it had been carrying had no alternative load path. "
"Each floor's collapse added its weight to the floor below — exactly the compounding load "
"mechanism modeled in Experiment 2 below.\n",
"\n",
"**The code response:**\n",
"\n",
"The Murrah collapse led the US General Services Administration and Department of Defense to develop "
"explicit **progressive collapse prevention guidelines** (GSA 2003, UFC 4-023-03). "
"These require engineers to show that losing any one primary member does not collapse more than a "
"limited zone. In probability terms: *P(floor fails | column lost) must be kept low* by providing "
"redundant load paths — the parallel-system principle from §14.1 applied to extreme events.\n",
"\n",
"> *The building did not collapse because the bomb was large. It collapsed because there was no "
"alternative load path once the columns were gone — conditional probability near 1.0, exactly as "
"the theory predicts.*\n",
]),

cell("markdown","exp2intro",[
"## 🔬 Interactive Experiment 2: Simulating Progressive Collapse\n",
"\n",
"The simulation below models a stack of floor panels. Each floor has a base failure probability p. "
"If the floor above has already failed, the load on this floor increases — raising its failure "
"probability according to a **simplified model** (failure probability scales with the square of the "
"load multiplier). This is not derived from any specific structural code or Hibbeler problem; "
"it is a conceptual illustration of how conditional failure probability grows. Real progressive "
"collapse analysis uses nonlinear dynamic models.\n",
"\n",
"Set the initial trigger probability and watch how many floors collapse on average.\n",
]),

cell("code","widget2",[
"def _progressive_collapse(p_base_pct, n_floors, n_sims):\n",
"    p_base = p_base_pct / 100\n",
"\n",
"    total_collapses = []\n",
"    for _ in range(n_sims):\n",
"        load_multiplier = 1.0\n",
"        collapsed = 0\n",
"        for _ in range(n_floors):\n",
"            # Failure probability increases with load multiplier\n",
"            p_this = min(p_base * load_multiplier**2, 1.0)\n",
"            if np.random.random() < p_this:\n",
"                collapsed += 1\n",
"                load_multiplier += 1.0   # next floor sees extra load\n",
"            else:\n",
"                load_multiplier = 1.0    # load redistributed; chain stops\n",
"                break\n",
"        total_collapses.append(collapsed)\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    # Distribution of collapse depth\n",
"    max_c = max(total_collapses) + 1\n",
"    ax1.hist(total_collapses, bins=range(0, max_c+1), color='firebrick',\n",
"        edgecolor='white', align='left', density=True)\n",
"    ax1.set_xlabel('Number of Floors Collapsed', fontsize=12)\n",
"    ax1.set_ylabel('Fraction of Simulations', fontsize=12)\n",
"    ax1.set_title(f'Progressive Collapse Depth  ({n_sims} simulations)', fontsize=13)\n",
"    ax1.annotate(\n",
"        f'Avg floors collapsed: {np.mean(total_collapses):.2f}\\nP(≥3 floors): {np.mean(np.array(total_collapses)>=3)*100:.1f}%',\n",
"        xy=(0.55, 0.82), xycoords='axes fraction', fontsize=10,\n",
"        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.9))\n",
"\n",
"    # Conditional probabilities by floor\n",
"    floors = list(range(1, 8))\n",
"    cond_probs = [min(p_base * m**2, 1.0)*100 for m in range(1, 8)]\n",
"    ax2.bar(floors, cond_probs, color='darkorange', edgecolor='white')\n",
"    ax2.set_xlabel('Floor (given all previous floors collapsed)', fontsize=12)\n",
"    ax2.set_ylabel('P(this floor fails | above failed) %', fontsize=12)\n",
"    ax2.set_title('How Conditional Probability Grows with Load', fontsize=13)\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"w_p  = widgets.FloatSlider(value=5.0, min=1.0, max=30.0, step=0.5,\n",
"    description='Base P(fail) % :', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"w_nf = widgets.IntSlider(value=10, min=4, max=30, step=1,\n",
"    description='Number of floors:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"w_ns = widgets.IntSlider(value=500, min=100, max=2000, step=100,\n",
"    description='Simulations:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"out2 = widgets.interactive_output(_progressive_collapse,\n",
"    {'p_base_pct': w_p, 'n_floors': w_nf, 'n_sims': w_ns})\n",
"display(widgets.VBox([w_p, w_nf, w_ns, out2]))\n",
]),

cell("markdown","review",[
"---\n",
"## 📋  Chapter 14 Review\n",
"\n",
"| Rule | Structural Meaning |\n",
"|------|-------------------|\n",
"| **Multiplication rule (independent AND)** | Series system survival = all members survive |\n",
"| **Multiplication rule (independent AND)** | Parallel system failure = all members fail |\n",
"| **Conditional probability** | P(member B fails \\| member A already failed) > P(member B fails) in a non-redundant system |\n",
"| **Addition rule (OR)** | P(at least one of n independent members fails) = 1 − (1−p)ⁿ |\n",
"\n",
"**The Big Idea:** The difference between a structure that stops at one member failing and one that collapses entirely is conditional probability. Redundant structures limit how much one failure raises the probability of the next. Non-redundant structures create conditional probability chains where each failure nearly guarantees the next — progressive collapse. This is why modern codes require alternative load paths: not as a luxury, but as a mathematical necessity for keeping conditional failure probabilities acceptably low.\n",
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
    out = os.path.join(os.path.dirname(__file__), '..', 'Chapter_14.ipynb')
    with open(out, 'w') as f: json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == '__main__': build_notebook()
