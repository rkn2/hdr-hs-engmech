"""
Generates Chapter_11_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch11 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 11: Understanding Randomness</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_11.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Law of Large Numbers; short-run variability vs. long-run stability; "
"sampling variability\n",
"- *Physics class*: Measurement uncertainty; material properties and tolerances; "
"why engineers use safety factors\n",
"\n",
"**Prerequisites:** Students should understand basic descriptive statistics (mean, standard deviation) "
"and have been introduced to the idea that repeated measurements vary.\n",
"\n",
"**Estimated time:** 45–55 minutes. Widget 1 (steel beam variability) takes about 20 minutes; "
"Widget 2 (concrete cylinder tests / ACI acceptance) takes about 25 minutes.\n",
"\n",
"**Pedagogical note:** The most common student misconception about randomness is the *gambler's fallacy* — "
"the belief that after several low values, the next must be high. Widget 1 is specifically designed to "
"surface this. Run it with n=5, ask students to predict the next result, then bump to n=50 and n=200 "
"to show that the mean stabilizes without any 'correction.' The concrete cylinder Widget 2 then connects "
"the same idea to a real quality-control decision students can reason about: would you accept or reject "
"this batch?\n",
"</div>\n",
])

EDU_ANSWER_KEY_1 = cell("markdown", "edu_ak1", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think (Widget 1)\n",
"\n",
"**1. Running mean at n=5 vs. n=200:** At n=5, the running mean swings wildly — often ±5–10 ksi "
"from the true mean (~55 ksi). By n=200, it has settled to within ~1 ksi. This is the Law of Large "
"Numbers in action: with more trials, the sample mean converges toward the population mean.\n",
"\n",
"**2. Why can't engineers just test one beam?** Because one measurement captures only one draw from "
"the distribution. It might be unusually strong (overconfident) or unusually weak (too conservative). "
"Testing many specimens gives a reliable estimate of the *distribution* — both the mean and the spread — "
"which is what safety factors are calibrated against.\n",
"\n",
"**3. What happens to spread as n increases?** The individual yield strength values keep varying "
"(the distribution doesn't change), but the *running mean* becomes more stable. Students sometimes "
"confuse 'the mean converges' with 'the measurements become more consistent' — they do not. "
"Each new beam is still drawn from the same variable population.\n",
"\n",
"**Common misconception to address:** If the first 10 beams all test above 57 ksi, does the next "
"one have to be lower? No. Each beam is independent. There is no 'correction' mechanism. "
"This is the gambler's fallacy.\n",
"</div>\n",
])

EDU_ANSWER_KEY_2 = cell("markdown", "edu_ak2", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think (Widget 2 — Concrete Cylinder Tests)\n",
"\n",
"**1. ACI 318 acceptance:** The ACI 318 standard requires that: (a) no individual cylinder test "
"falls below f'c − 500 psi, AND (b) the average of any three consecutive tests meets or exceeds f'c. "
"The widget shows when these criteria are violated. A batch with many failures near the spec limit "
"*should* trigger a rejection review, even if the average looks acceptable.\n",
"\n",
"**2. Why test multiple cylinders per batch?** Same reason as Widget 1: one cylinder could be an "
"outlier. The ACI criterion uses averages of three consecutive tests precisely to reduce the chance "
"of accepting a genuinely weak batch because one test happened to be high.\n",
"\n",
"**3. Connection to safety factors:** The specified strength f'c = 4000 psi is the *minimum* the "
"engineer assumes in design. The production mean (~4600 psi) is deliberately set higher so that "
"even the lower tail of the distribution stays above 4000 psi. This margin is not waste — "
"it is a direct consequence of variability.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — Quebec Bridge Case Study\n",
"\n",
"The Quebec Bridge (1907) is one of the clearest historical examples of *not taking variability seriously* "
"in structural engineering. The design load calculations used the nominal steel weight (400 tons), "
"but as construction progressed and the actual weight grew toward 1800 tons, the chief engineer "
"Theodore Cooper continued to approve work without field verification.\n",
"\n",
"**Key point for students:** This is not just a calculation error — it is a failure of statistical "
"thinking. Cooper treated a growing, uncertain quantity (the actual structure weight) as if it were "
"a fixed known value. The equivalent in statistics: treating a sample mean as if it were the "
"population mean, without accounting for uncertainty.\n",
"\n",
"**Physics connection:** The collapse was a compression failure in the lower chord near the anchor arm. "
"The actual stress (σ = F/A) exceeded the material's yield strength because F (the actual load) "
"was far larger than F (the assumed design load). The formula is simple; the failure was in "
"the *inputs*, not the math.\n",
"\n",
"**Emotional note:** 75 workers died. This is still the deadliest construction accident in Canadian "
"history. Frame the discussion around the professional responsibility created by uncertainty, "
"not just the math.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. Gambler's fallacy (warm-up):** A fair coin has come up heads 8 times in a row. "
"What is the probability the next flip is tails? *(Answer: 50% — each flip is independent.) "
"How does this connect to running average of beam strengths? Both demonstrate that past results "
"don't 'load up' a correction in a random process.*\n",
"\n",
"**2. Sample size trade-offs (pair discussion):** Testing more concrete cylinders gives a better "
"estimate of batch strength — but tests cost time and money. If you were the structural engineer "
"of record for a new hospital, how many cylinders per batch would you want? How does the stakes "
"of the project affect your answer? *(Guide toward: higher consequence → more testing. "
"This is the cost-benefit logic behind sampling theory.)*\n",
"\n",
"**3. Material consistency (small group):** Modern steel is produced in large continuous casts "
"with tight quality control. Concrete is mixed on-site from local materials that vary by season "
"and supplier. Which material would you expect to have a *smaller* coefficient of variation (CV = σ/μ)? "
"Why? *(Steel typically CV ≈ 5–7%; concrete CV ≈ 8–12% for compressive strength.) "
"What does this imply for safety factors?*\n",
"\n",
"**4. Extension (homework):** The Law of Large Numbers is sometimes misunderstood as meaning "
"'things even out over time.' Find an example from sports statistics, medicine, or finance where "
"someone made a decision based on the gambler's fallacy. Explain the error and what the LLN "
"actually predicts.\n",
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
            # Ch11 has no reflect cells; inject Widget 1 answer key here (after first widget + case study)
            result.append(EDU_ANSWER_KEY_1)
            result.append(EDU_CASE_NOTE)
        elif cid == "exp2intro":
            # Widget 2 answer key appears after its intro, before students run it
            result.append(EDU_ANSWER_KEY_2)
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_11_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
