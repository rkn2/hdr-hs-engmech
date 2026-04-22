"""
Generates Chapter_15_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch15 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 15: Probability Models</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_15.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Normal distribution; z-scores; area under the normal curve; "
"overlap of two distributions\n",
"- *Physics class*: Stress and strength as physical quantities; why safety factors exist; "
"factor of safety as a design parameter\n",
"\n",
"**Prerequisites:** Students should understand the normal distribution conceptually "
"(bell-shaped, described by mean and standard deviation) and be able to read z-score tables "
"or use a calculator/software to find areas under the curve.\n",
"\n",
"**Estimated time:** 50–60 minutes. The load-vs-resistance overlap concept (Widget 1) needs "
"15–20 minutes of setup discussion before students explore it. Budget time to make sure "
"students understand that the *overlap area* = P(failure).\n",
"\n",
"**Pedagogical note:** The reliability index β is just a z-score applied to structural safety — "
"it measures how many standard deviations of margin separate the mean resistance from the "
"mean load. Students who understand z-scores already understand β intuitively. The key move "
"is reframing 'safety factor' from an arbitrary number to a probability statement: "
"β = 3.5 means P(failure) ≈ 1 in 4,300. That number gives the safety factor meaning.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — LRFD Calibration Case Study\n",
"\n",
"The shift from ASD (Allowable Stress Design) to LRFD (Load and Resistance Factor Design) in US "
"structural codes during the 1980s–90s is one of the most consequential applications of "
"probability theory in engineering practice.\n",
"\n",
"**ASD approach:** Choose a safety factor (e.g., 1.67) and require:\n"
"actual stress ≤ F_y / 1.67. The safety factor is a single number — it doesn't distinguish "
"between a load that is well-known (dead load) and one that is highly uncertain (wind load).\n",
"\n",
"**LRFD approach:** Apply *different* factors to different loads based on their uncertainty:\n"
"1.2D + 1.6L ≤ φ R_n, where φ accounts for resistance uncertainty. "
"More uncertain loads get larger factors. This is probability-aware design.\n",
"\n",
"**The β = 3.5 target:** Ellingwood et al. (1980) calibrated LRFD load and resistance factors "
"to achieve a reliability index β ≈ 3.5 for typical members under typical load combinations. "
"This corresponds to roughly P(failure) ≈ 1 in 4,300 per year — a level considered appropriate "
"for redundant structural members. Non-redundant or fracture-critical members may use β = 4.0 or higher.\n",
"\n",
"**For students:** This is statistics being used to *design* the rules of engineering — "
"not just to analyze data after the fact.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. β as a z-score (warm-up):** If the margin between mean resistance and mean load is "
"35 kips, and the combined standard deviation of resistance and load is 10 kips, "
"what is β? What is the approximate probability of failure? "
"*(β = 35/10 = 3.5; P(failure) ≈ 1/4,300.)*\n",
"\n",
"**2. ASD vs. LRFD (pair discussion):** An old building was designed with a safety factor "
"of 1.5 under ASD. Does that tell you anything about the probability of failure? "
"Why or why not? *(No — the safety factor doesn't encode the variability of the loads or "
"the resistance. Two structures with the same safety factor can have very different failure "
"probabilities depending on how variable their loads and materials are.)*\n",
"\n",
"**3. Challenger connection (small group):** On January 27, 1986, engineers at Morton Thiokol "
"warned NASA not to launch the Space Shuttle Challenger because O-ring performance was uncertain "
"at low temperatures. The decision was made to launch anyway. "
"The O-rings failed; the shuttle was destroyed 73 seconds after launch, killing all seven crew. "
"The engineers had data showing O-ring damage correlated with temperature — "
"but the analysis was incomplete (they excluded flights with no damage from the regression). "
"How does this connect to the load-resistance overlap model? "
"*(The resistance distribution shifted left in cold temperatures, increasing overlap with the "
"load distribution — but this wasn't quantified properly.)*\n",
"\n",
"**4. Extension (homework):** Research the difference between ASD and LRFD for one "
"structural material (steel, concrete, or timber). Find one specific design situation "
"where LRFD gives a *different* (larger or smaller) required member size than ASD. "
"Explain why the difference occurs.\n",
"</div>\n",
])

def build_cells():
    result = []
    result.append(EDU_BANNER)
    for sc in STUDENT_CELLS:
        result.append(sc)
        cid = sc.get("id", "")
        if cid == "photo":
            result.append(EDU_CONTEXT)
        elif cid == "casestudy":
            result.append(EDU_CASE_NOTE)
        elif cid == "review":
            result.append(EDU_DISCUSSION)
    return result

def build_notebook():
    nb = {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.8.0"},
            "colab": {"provenance": []},
        },
        "cells": build_cells(),
    }
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_15_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
