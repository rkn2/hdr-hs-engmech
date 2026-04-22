"""
Generates Chapter_11.ipynb — Understanding Randomness (Structural Engineering version)
Grounded in Hibbeler Structural Analysis 8th ed., Chapter 1 (material variability, load uncertainty)
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
"# Chapter 11: Understanding Randomness in Structural Engineering\n",
"## Why No Two Steel Beams Are Exactly the Same\n",
"\n",
"**Learning Objectives:**\n",
"- Explain what makes a process random vs. predictable\n",
"- Demonstrate the Law of Large Numbers using structural material tests\n",
"- Distinguish short-run variability from long-run stability\n",
"- Connect randomness in material properties to how engineers design with safety factors\n",
]),

cell("markdown","photo",[
"<center>\n",
"<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Compressive_strength_testing_machine.jpg/640px-Compressive_strength_testing_machine.jpg' width='480' />\n",
"\n",
"<em>A concrete cylinder being crushed in a compression testing machine (ASTM C39). "
"Structural engineers test batches of cylinders to estimate actual strength — "
"a direct application of the Law of Large Numbers. (Wikimedia Commons — CC BY-SA.)</em>\n",
"</center>\n",
"\n",
"---\n",
]),

cell("code","setup",[
"import subprocess, sys\n",
"subprocess.run([sys.executable,'-m','pip','install','ipywidgets','--quiet'])\n",
"import numpy as np\n",
"import matplotlib.pyplot as plt\n",
"import ipywidgets as widgets\n",
"from IPython.display import display\n",
"%matplotlib inline\n",
"np.random.seed(11)\n",
"\n",
"# ASTM A572 Grade 50 structural steel — nominal yield strength 50 ksi\n",
"# NOTE: The values below (mean ~55 ksi, SD ~3.5 ksi) are illustrative, not from Hibbeler directly.\n",
"# They reflect realistic ranges reported in structural reliability literature (e.g., AISC LRFD calibration\n",
"# studies). Hibbeler references this steel grade but does not tabulate statistical distributions.\n",
"TRUE_MEAN_KSI = 55.0\n",
"TRUE_SD_KSI   = 3.5\n",
"POPULATION    = np.random.normal(TRUE_MEAN_KSI, TRUE_SD_KSI, 10000)\n",
"print('ASTM A572 Grade 50 steel population (10,000 simulated mill coupons)')\n",
"print('  [Values are illustrative; see AISC LRFD calibration studies for sources]')\n",
"print(f'  Nominal minimum yield strength: 50 ksi')\n",
"print(f'  Simulated true mean:  {TRUE_MEAN_KSI} ksi')\n",
"print(f'  Simulated true SD:    {TRUE_SD_KSI} ksi')\n",
"print(f'  Samples below 50 ksi: {(POPULATION < 50).mean()*100:.1f}%  (these would fail the spec)')\n",
]),

cell("markdown","why",[
"## 11.1  Randomness in Structural Materials\n",
"\n",
"When a steel mill produces a W18×97 wide-flange beam, every beam comes out slightly different. The rolling process, cooling rate, and chemical composition of each heat of steel introduce unavoidable variation. This is not sloppy manufacturing — it is physical reality.\n",
"\n",
"**ASTM A572 Grade 50 steel** (one of the most common structural steels, discussed throughout Hibbeler) has a *nominal* minimum yield strength of **50 ksi**. The statistical values used here — mean ~55 ksi, SD ~3.5 ksi — are *illustrative*, based on ranges reported in structural reliability research. Hibbeler references A572 steel throughout but does not tabulate its statistical distribution; that data comes from AISC calibration studies. But real mill data shows that:\n",
"\n",
"- The **actual mean** yield strength is closer to **55 ksi** — mills intentionally produce above the minimum\n",
"- Individual coupon tests scatter around that mean with a standard deviation of about **3–4 ksi**\n",
"- A small percentage of coupons will test *below* 50 ksi even from a compliant heat\n",
"\n",
"This is why structural codes require testing **multiple specimens**, not just one. A single test result is random. The average of many tests is not.\n",
"\n",
"That principle — that averages stabilize even when individual results do not — is called the **Law of Large Numbers**.\n",
]),

cell("markdown","exp1intro",[
"## 🔬 Interactive Experiment 1: The Law of Large Numbers in a Steel Mill\n",
"\n",
"Imagine you are a quality-control engineer. You pull steel coupons from a production run and test their yield strength. Each test gives you a random result.\n",
"\n",
"- With **1 test**, your estimate of the batch's average strength could be wildly off.\n",
"- With **50 tests**, your estimate is much more reliable.\n",
"- With **200 tests**, you have a very accurate picture.\n",
"\n",
"Run the simulation below and watch how the running average of coupon tests converges toward the true mean as the number of tests increases.\n",
]),

cell("code","widget1",[
"def _lln_plot(n_tests):\n",
"    sample = np.random.choice(POPULATION, size=n_tests, replace=False)\n",
"    running_avg = np.cumsum(sample) / np.arange(1, n_tests + 1)\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    # Left: individual test results\n",
"    ax1.scatter(range(1, n_tests+1), sample, color='steelblue', alpha=0.5, s=15, label='Individual test')\n",
"    ax1.axhline(TRUE_MEAN_KSI, color='black', lw=2, ls='--', label=f'True mean: {TRUE_MEAN_KSI} ksi')\n",
"    ax1.axhline(50, color='firebrick', lw=1.5, ls=':', label='ASTM minimum: 50 ksi')\n",
"    ax1.set_xlabel('Test number', fontsize=12)\n",
"    ax1.set_ylabel('Yield Strength (ksi)', fontsize=12)\n",
"    ax1.set_title(f'Individual Coupon Tests  (n = {n_tests})', fontsize=13)\n",
"    ax1.legend(fontsize=10)\n",
"\n",
"    # Right: running average\n",
"    ax2.plot(range(1, n_tests+1), running_avg, color='steelblue', lw=2, label='Running average')\n",
"    ax2.axhline(TRUE_MEAN_KSI, color='black', lw=2, ls='--', label=f'True mean: {TRUE_MEAN_KSI} ksi')\n",
"    ax2.fill_between(range(1, n_tests+1),\n",
"        TRUE_MEAN_KSI - TRUE_SD_KSI, TRUE_MEAN_KSI + TRUE_SD_KSI,\n",
"        alpha=0.12, color='steelblue', label='±1 SD band')\n",
"    ax2.set_xlabel('Number of Tests', fontsize=12)\n",
"    ax2.set_ylabel('Running Average Yield Strength (ksi)', fontsize=12)\n",
"    ax2.set_title('Running Average Converges to True Mean', fontsize=13)\n",
"    ax2.legend(fontsize=10)\n",
"    final_err = abs(running_avg[-1] - TRUE_MEAN_KSI)\n",
"    ax2.annotate(f'Error after {n_tests} tests: {final_err:.2f} ksi',\n",
"        xy=(0.03, 0.08), xycoords='axes fraction', fontsize=10,\n",
"        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"w_n = widgets.IntSlider(value=20, min=1, max=300, step=1,\n",
"    description='Number of tests:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"out1 = widgets.interactive_output(_lln_plot, {'n_tests': w_n})\n",
"display(widgets.VBox([w_n, out1]))\n",
]),

cell("markdown","casestudy",[
"---\n",
"## ⚠️  Why Testing Standards Require Multiple Specimens\n",
"\n",
"Before ASTM formalized multi-specimen testing requirements, some engineers accepted single-coupon test results as proof of material compliance. This was dangerous precisely because of the Law of Large Numbers — or rather, its inverse:\n",
"\n",
"> *A single test result tells you almost nothing about the true mean of the population.*\n",
"\n",
"**ASTM A6** (the standard governing structural steel) now requires a minimum number of tension tests per heat of steel, and specifies that the reported yield strength must satisfy statistical requirements — not just a single pass.\n",
"\n",
"The **Quebec Bridge collapse of 1907** is a sobering early example. The bridge's chief engineer, Theodore Cooper, approved the use of heavier steel members based on limited material tests and calculations he performed remotely — without physically being at the site. When a bottom chord member buckled and the bridge collapsed (killing 75 workers), the investigation found that the actual dead load of the structure had been systematically underestimated from the start. A random sample of a few members had been tested and deemed acceptable; the full population of members had not been.\n",
"\n",
"> *Randomness does not go away when you ignore it. It simply waits.*\n",
]),

cell("markdown","exp2intro",[
"## 🔬 Interactive Experiment 2: Short-Run Surprises in Concrete Cylinder Tests\n",
"\n",
"When a structural concrete pour is placed, ASTM C39 requires engineers to cast and crush "
"companion cylinders to verify that the concrete reached its specified compressive strength f'c. "
"Each cylinder gives a random result — and with only a few tests, the sample mean bounces around.\n",
"\n",
"The simulation below shows what happens as more cylinders are tested from the same pour. "
"Watch how the running maximum (the strongest cylinder seen so far) stabilizes, "
"and how the distribution of strengths takes shape.\n",
]),

cell("code","widget2",[
"# Concrete cylinder compression tests — ASTM C39\n",
"# Specified f'c = 4000 psi (a common value for structural slabs and beams)\n",
"# Typical production: mean ~4600 psi (batching plant overshoots to meet spec),\n",
"# SD ~380 psi (coefficient of variation ~8%, typical for ready-mix concrete)\n",
"CONC_FC_SPEC = 4000   # psi, specified minimum compressive strength\n",
"CONC_MEAN    = 4600   # psi, typical production mean\n",
"CONC_SD      = 380    # psi, typical standard deviation\n",
"CONC_POP     = np.abs(np.random.normal(CONC_MEAN, CONC_SD, 50000))\n",
"\n",
"def _cylinder_plot(n_tests):\n",
"    sample = np.random.choice(CONC_POP, size=n_tests, replace=True)\n",
"    running_max = np.maximum.accumulate(sample)\n",
"\n",
"    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
"\n",
"    ax1.plot(range(1, n_tests+1), running_max, color='darkorange', lw=1.5)\n",
"    ax1.axhline(np.percentile(CONC_POP, 99), color='firebrick', lw=2, ls='--',\n",
"        label='99th percentile strength')\n",
"    ax1.axhline(CONC_FC_SPEC, color='gray', lw=1.5, ls=':',\n",
"        label=f\"Specified f'c = {CONC_FC_SPEC} psi\")\n",
"    ax1.set_xlabel('Number of Cylinder Tests', fontsize=12)\n",
"    ax1.set_ylabel(\"Compressive Strength (psi)\", fontsize=12)\n",
"    ax1.set_title('Running Maximum — Strongest Cylinder Seen So Far', fontsize=13)\n",
"    ax1.legend(fontsize=10)\n",
"\n",
"    ax2.hist(sample, bins=40, color='darkorange', edgecolor='white', alpha=0.75)\n",
"    ax2.axvline(np.mean(sample), color='black', lw=2, ls='--',\n",
"        label=f'Sample mean: {np.mean(sample):.0f} psi')\n",
"    ax2.axvline(CONC_FC_SPEC, color='firebrick', lw=2, ls=':',\n",
"        label=f\"Specified f'c = {CONC_FC_SPEC} psi\")\n",
"    pct_below = (sample < CONC_FC_SPEC).mean() * 100\n",
"    ax2.set_xlabel(\"Compressive Strength f'c (psi)\", fontsize=12)\n",
"    ax2.set_ylabel('Number of Cylinders', fontsize=12)\n",
"    ax2.set_title(f'Distribution of {n_tests} Cylinder Tests', fontsize=13)\n",
"    ax2.legend(fontsize=10)\n",
"    ax2.annotate(f\"{pct_below:.1f}% of cylinders\\nbelow specified f'c\",\n",
"        xy=(0.03, 0.80), xycoords='axes fraction', fontsize=10,\n",
"        bbox=dict(boxstyle='round',\n",
"            facecolor='mistyrose' if pct_below > 10 else 'lightgreen', alpha=0.9))\n",
"    plt.tight_layout()\n",
"    plt.show()\n",
"\n",
"w_n2 = widgets.IntSlider(value=50, min=5, max=500, step=5,\n",
"    description='Cylinder tests:', style={'description_width':'initial'},\n",
"    layout=widgets.Layout(width='430px'))\n",
"out2 = widgets.interactive_output(_cylinder_plot, {'n_tests': w_n2})\n",
"display(widgets.VBox([w_n2, out2]))\n",
]),

cell("markdown","review",[
"---\n",
"## 📋  Chapter 11 Review\n",
"\n",
"| Term | Meaning |\n",
"|------|--------|\n",
"| **Random process** | Individual outcomes are unpredictable; the long-run pattern is stable |\n",
"| **Law of Large Numbers** | As sample size grows, the sample mean converges to the true population mean |\n",
"| **Short-run variability** | Individual results fluctuate widely around the true mean |\n",
"| **Long-run stability** | The average of many results settles near the true mean |\n",
"| **Simulation** | Using a computer to repeat a random process many times and observe the pattern |\n",
"\n",
"**The Big Idea:** Structural engineers rely on the Law of Large Numbers every time they use a code-specified load or material strength. Those values were derived from thousands of tests and measurements. No single test result tells you much — but the average of many tests is a reliable guide for design. Randomness, understood correctly, is not a source of danger. Ignoring it is.\n",
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
    out = os.path.join(os.path.dirname(__file__), '..', 'Chapter_11.ipynb')
    with open(out, 'w') as f: json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == '__main__': build_notebook()
