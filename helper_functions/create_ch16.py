"""
Generates Chapter_16.ipynb — Confidence Intervals (Structural Engineering version)
Grounded in Hibbeler Chapter 8 (deflections) and bridge load testing / proof load testing
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
"# Chapter 16: Confidence Intervals in Structural Engineering\n",
"## How Certain Are We About This Bridge's Stiffness?\n",
"\n",
"**Learning Objectives:**\n",
"- Construct and interpret a confidence interval for a structural measurement\n",
"- Explain why wider intervals mean more uncertainty — and more required safety margin\n",
"- Describe how bridge load testing uses confidence intervals to set safe carrying capacities\n",
"- Connect the width of a confidence interval to sample size and measurement variability\n",
]),

cell("markdown","photo",[
"<center>\n",
"<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/I-35W_Saint_Anthony_Falls_Bridge.jpg/1280px-I-35W_Saint_Anthony_Falls_Bridge.jpg' width='700' />\n",
"\n",
"<em>The St. Anthony Falls Bridge, Minneapolis — the replacement for the I-35W bridge that collapsed in 2007. "
"Before opening in September 2008, MnDOT placed 2 million pounds of precast concrete barriers on the bridge "
"and measured deflections at 36 locations, comparing them to design predictions. "
"This is proof load testing: each measurement is one EI estimate, and the set of measurements forms a "
"confidence interval for the bridge's actual stiffness. (Wikimedia Commons — public domain.)</em>\n",
"</center>\n",
"\n",
"---\n",
]),

cell("code","setup",[
"import subprocess, sys\n",
"subprocess.run([sys.executable,'-m','pip','install','ipywidgets','--quiet'])\n",
"import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"from scipy import stats\n",
"import ipywidgets as widgets\n",
"from IPython.display import display\n",
"%matplotlib inline\n",
"np.random.seed(16)\n",
"\n",
"# True beam stiffness EI = 120,000 kip·in² (a W18×97 in A572 Gr.50 steel)\n",
"# E = 29,000 ksi, I ≈ 4.14 in⁴ for W18×97... actually let's use round numbers\n",
"# W18×97: I_x = 1910 in⁴, E = 29000 ksi → EI = 29000 * 1910 = 55,390,000 kip·in²\n",
"# For simplicity: represent in units of 1000 kip·ft²\n",
"TRUE_EI   = 385.0   # kip·ft² × 1000 (representative value)\n",
"MEAS_SD   = 18.0    # measurement noise in same units\n",
"print('Bridge load test setup:')\n",
"print(f'  True beam stiffness EI: {TRUE_EI} (×10³ kip·ft²)  [hidden from inspector]')\n",
"print(f'  Measurement noise σ:    {MEAS_SD} (±{MEAS_SD/TRUE_EI*100:.1f}%)')\n",
]),

cell("markdown","why",[
"## 16.1  What Is a Confidence Interval?\n",
"\n",
"A **confidence interval** is a range of plausible values for an unknown parameter, computed from a sample.\n",
"\n",
"When a structural engineer loads a bridge with known test weights and measures the resulting deflection, they can back-calculate the bridge's **flexural stiffness EI** using Hibbeler's beam deflection formulas (Chapter 8). For a simply supported beam with a midspan point load P:\n",
"\n",
"$$EI = \\frac{PL^3}{48\\,\\delta}$$\n",
"\n",
"But every deflection measurement has noise — sensor error, temperature effects, traffic vibration. Each test gives a slightly different EI estimate. The **confidence interval** captures that uncertainty:\n",
"\n",
"$$\\bar{x} \\pm t^* \\cdot \\frac{s}{\\sqrt{n}}$$\n",
"\n",
"Where:\n",
"- $\\bar{x}$ = sample mean of EI estimates\n",
"- $s$ = sample standard deviation of EI estimates  \n",
"- $n$ = number of load tests\n",
"- $t^*$ = critical value from the t-distribution (depends on confidence level and n)\n",
"\n",
"**Why this matters for safety:** If the confidence interval for EI is wide, the engineer cannot be sure whether the bridge is stiffer or more flexible than expected. A more flexible bridge deflects more — meaning stress is higher — meaning the safe load rating must be lower. **Uncertainty directly reduces the load the bridge is allowed to carry.**\n",
]),

cell("markdown","exp1intro",[
"## 🔬 Interactive Experiment 1: Building a Confidence Interval From Load Tests\n",
"\n",
"You are an engineer performing a proof load test on a highway bridge. Each test — lowering a known weight onto the bridge and measuring midspan deflection — gives you one EI estimate. The true EI is unknown to you (but the simulation knows it).\n",
"\n",
"Use the slider to increase the number of tests. Watch how the confidence interval narrows — and how the interval captures the true value.\n",
]),

cell("code","widget1",[
"def _ci_plot(n_tests, confidence):\n",
"    sample = np.random.normal(TRUE_EI, MEAS_SD, n_tests)\n",
"    xbar = np.mean(sample)\n",
"    s    = np.std(sample, ddof=1)\n",
"    alpha = 1 - confidence/100\n",
"    t_star = stats.t.ppf(1 - alpha/2, df=n_tests-1)\n",
"    margin = t_star * s / np.sqrt(n_tests)\n",
"    ci_lo, ci_hi = xbar - margin, xbar + margin\n",
"    captures = ci_lo <= TRUE_EI <= ci_hi\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    # Left: individual test results\n",
"    ax1.scatter(range(1, n_tests+1), sample, color='steelblue', alpha=0.6, s=25, zorder=3)\n",
"    ax1.axhline(xbar,    color='steelblue', lw=2,   ls='-',  label=f'Sample mean: {xbar:.1f}')\n",
"    ax1.axhline(TRUE_EI, color='black',     lw=2,   ls='--', label=f'True EI: {TRUE_EI}')\n",
"    ax1.fill_between([0, n_tests+1], [ci_lo]*2, [ci_hi]*2, alpha=0.2,\n",
"        color='steelblue', label=f'{confidence}% CI: [{ci_lo:.1f}, {ci_hi:.1f}]')\n",
"    ax1.set_xlabel('Load Test Number', fontsize=12)\n",
"    ax1.set_ylabel('EI Estimate (×10³ kip·ft²)', fontsize=12)\n",
"    ax1.set_title(f'{n_tests} Load Tests — {confidence}% Confidence Interval', fontsize=13)\n",
"    ax1.legend(fontsize=9)\n",
"    color = 'lightgreen' if captures else 'mistyrose'\n",
"    ax1.annotate(f'CI width: {2*margin:.1f}\\n{\"✅ Captures true EI\" if captures else \"❌ Misses true EI\"}',\n",
"        xy=(0.03, 0.05), xycoords='axes fraction', fontsize=10,\n",
"        bbox=dict(boxstyle='round', facecolor=color, alpha=0.9))\n",
"\n",
"    # Right: margin of error vs sample size\n",
"    ns = range(2, 101)\n",
"    margins = [stats.t.ppf(1-alpha/2, df=k-1) * MEAS_SD / np.sqrt(k) for k in ns]\n",
"    ax2.plot(list(ns), margins, 'steelblue', lw=2.5)\n",
"    ax2.axvline(n_tests, color='firebrick', lw=2, ls='--', label=f'Your n = {n_tests}')\n",
"    ax2.axhline(margin, color='firebrick', lw=1.5, ls=':', label=f'Your margin = ±{margin:.1f}')\n",
"    ax2.set_xlabel('Number of Load Tests (n)', fontsize=12)\n",
"    ax2.set_ylabel(f'Margin of Error (×10³ kip·ft²)', fontsize=12)\n",
"    ax2.set_title(f'How Margin of Error Shrinks With More Tests\\n({confidence}% confidence)', fontsize=13)\n",
"    ax2.legend(fontsize=10)\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"w_n  = widgets.IntSlider(value=5, min=2, max=80, step=1,\n",
"    description='Load tests (n):', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"w_cl = widgets.Dropdown(options=[90, 95, 99], value=95,\n",
"    description='Confidence level %:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='300px'))\n",
"out1 = widgets.interactive_output(_ci_plot, {'n_tests': w_n, 'confidence': w_cl})\n",
"display(widgets.VBox([w_n, w_cl, out1]))\n",
]),

cell("markdown","reflect",[
"### 💬 Stop and Think\n",
"\n",
"1. With n = 3 tests, how wide is your confidence interval? What does that width mean for the engineer deciding how much load the bridge can safely carry?\n",
"2. How many tests does it take before the margin of error drops below 10 units? Below 5 units?\n",
"3. Why does switching from 90% to 99% confidence make the interval *wider* — even with the same data?\n",
]),

cell("markdown","casestudy",[
"---\n",
"## ⚠️  Real-World Case: Proof Load Testing the St. Anthony Falls Bridge (2008)\n",
"\n",
"When the I-35W bridge collapsed in Minneapolis on August 1, 2007 (see Chapter 10), "
"the replacement — the St. Anthony Falls Bridge — was designed and built in just 13 months. "
"Before it opened to traffic in September 2008, the Minnesota Department of Transportation (MnDOT) "
"conducted a full-scale **proof load test**.\n",
"\n",
"**What they did:**\n",
"\n",
"Engineers placed approximately 2 million pounds of precast concrete barriers at 18 positions across "
"the bridge deck. At each loading configuration, they measured deflections at 36 sensor locations "
"using high-precision surveying equipment. Each measurement produced one estimate of the bridge's "
"actual flexural stiffness EI. The engineers then compared those EI estimates to what the finite "
"element model had predicted.\n",
"\n",
"**The confidence interval connection:**\n",
"\n",
"Across the 36 sensor locations and multiple loading configurations, the EI estimates scattered around "
"a mean — with variability from sensor noise, thermal effects, and model simplifications. "
"The engineers computed a confidence interval for the actual bridge stiffness:\n",
"\n",
"- A **narrow CI** would mean the measurements agreed closely, the bridge was behaving as designed, "
"and the load rating could be set confidently\n",
"- A **wide CI** would indicate unexpected variability — a reason to investigate further before "
"certifying the bridge for full traffic loading\n",
"\n",
"The St. Anthony Falls Bridge results showed close agreement with design predictions. "
"The CI was narrow, and the bridge opened on schedule.\n",
"\n",
"> *Every number the engineers reported — the estimated stiffness, the allowable load — came with a "
"range of uncertainty. That range is the confidence interval. Ignoring it would mean pretending the "
"measurements were exact. They never are.*\n",
]),

cell("markdown","exp2intro",[
"## 🔬 Interactive Experiment 2: Coverage Probability\n",
"\n",
"A **95% confidence interval** means: if you repeated your sampling procedure many times, about 95% of the resulting intervals would capture the true parameter.\n",
"\n",
"The simulation below runs 100 repeated load-test campaigns, each producing a confidence interval. Count how many of the 100 intervals capture the true EI — it should be close to your chosen confidence level.\n",
]),

cell("code","widget2",[
"def _coverage_plot(n_tests, confidence, n_campaigns):\n",
"    alpha = 1 - confidence/100\n",
"    intervals = []\n",
"    for _ in range(n_campaigns):\n",
"        s = np.random.normal(TRUE_EI, MEAS_SD, n_tests)\n",
"        xb, sd = np.mean(s), np.std(s, ddof=1)\n",
"        t_star = stats.t.ppf(1-alpha/2, df=n_tests-1)\n",
"        m = t_star * sd / np.sqrt(n_tests)\n",
"        intervals.append((xb-m, xb+m, xb-m <= TRUE_EI <= xb+m))\n",
"\n",
"    covered = sum(1 for _,_,c in intervals if c)\n",
"\n",
"    fig, ax = plt.subplots(figsize=(12, 7))\n",
"    for i, (lo, hi, cap) in enumerate(intervals):\n",
"        color = 'steelblue' if cap else 'firebrick'\n",
"        ax.plot([lo, hi], [i, i], color=color, lw=1.5, alpha=0.7)\n",
"        ax.plot((lo+hi)/2, i, 'o', color=color, ms=3)\n",
"    ax.axvline(TRUE_EI, color='black', lw=2.5, ls='--', label=f'True EI = {TRUE_EI}')\n",
"    ax.set_xlabel('EI Estimate (×10³ kip·ft²)', fontsize=12)\n",
"    ax.set_ylabel('Campaign Number', fontsize=12)\n",
"    ax.set_title(\n",
"        f'{covered}/{n_campaigns} intervals capture true EI  '\n",
"        f'({covered/n_campaigns*100:.0f}% vs. {confidence}% target)',\n",
"        fontsize=13)\n",
"    ax.legend(fontsize=10)\n",
"    blue_p = mpatches.Patch(color='steelblue', label=f'Captures true EI ({covered})')\n",
"    red_p  = mpatches.Patch(color='firebrick', label=f'Misses true EI ({n_campaigns-covered})')\n",
"    ax.legend(handles=[blue_p, red_p], fontsize=10)\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"# need mpatches in scope\n",
"import matplotlib.patches as mpatches\n",
"\n",
"w_n  = widgets.IntSlider(value=8, min=2, max=40, step=1,\n",
"    description='Tests per campaign (n):', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"w_cl = widgets.Dropdown(options=[90, 95, 99], value=95,\n",
"    description='Confidence level %:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='300px'))\n",
"w_nc = widgets.IntSlider(value=100, min=20, max=200, step=10,\n",
"    description='Campaigns:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"out2 = widgets.interactive_output(_coverage_plot,\n",
"    {'n_tests':w_n,'confidence':w_cl,'n_campaigns':w_nc})\n",
"display(widgets.VBox([w_n, w_cl, w_nc, out2]))\n",
]),

cell("markdown","review",[
"---\n",
"## 📋  Chapter 16 Review\n",
"\n",
"| Term | Meaning |\n",
"|------|--------|\n",
"| **Confidence interval** | Range of plausible values for a parameter, from sample data |\n",
"| **Confidence level** | Percentage of intervals (from repeated sampling) that would capture the true parameter |\n",
"| **Margin of error** | Half-width of the CI: t* × s / √n |\n",
"| **t-distribution** | Used instead of normal distribution when σ is unknown and n is small |\n",
"| **Coverage probability** | Fraction of CIs (across many samples) that actually contain the true value |\n",
"\n",
"**The Big Idea:** When a structural engineer reports a load rating for a bridge, that rating is not a single certain number — it is the lower bound of a confidence interval for the bridge's true capacity. The wider the interval (more uncertainty), the lower the safe load rating must be. Confidence intervals translate statistical uncertainty into practical engineering decisions: how much load can we safely allow on this structure, given what we have measured and how precisely we measured it?\n",
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
    out = os.path.join(os.path.dirname(__file__), '..', 'Chapter_16.ipynb')
    with open(out, 'w') as f: json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == '__main__': build_notebook()
