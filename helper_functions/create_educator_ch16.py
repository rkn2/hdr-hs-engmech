"""
Generates Chapter_16_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch16 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 16: Confidence Intervals</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_16.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Confidence intervals; margin of error; effect of sample size and "
"confidence level on interval width; interpretation of 'confidence'\n",
"- *Physics class*: Measurement uncertainty; how repeated measurements reduce uncertainty; "
"deflection as a measurable physical quantity\n",
"\n",
"**Prerequisites:** Students should understand the normal distribution, standard deviation, "
"and the concept of a sampling distribution.\n",
"\n",
"**Estimated time:** 50–60 minutes. The coverage probability simulation (Widget 2) takes "
"the longest — let students run it at different confidence levels and observe how often "
"the true value falls inside vs. outside the interval.\n",
"\n",
"**Pedagogical note:** The most persistent confidence interval misconception is that "
"'95% confidence' means 'there is a 95% probability the true value is in this interval.' "
"The correct interpretation — 95% of intervals *constructed by this method* will contain "
"the true value — is subtle. Widget 2 makes this concrete: students watch hundreds of "
"intervals being built and count how many capture the true deflection. "
"This physical demonstration is far more effective than a verbal explanation alone.\n",
"</div>\n",
])

EDU_ANSWER_KEY = cell("markdown", "edu_ak", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think\n",
"\n",
"**1. Width of CI at n = 3 and what it means for load rating:**\n"
"With only 3 measurements, the margin of error is large — typically ±15–25 units depending "
"on the simulated variability. For a load rating decision, a wide interval means the engineer "
"cannot be confident the bridge's true stiffness is close to the measured mean. "
"The conservative response is to set a lower safe load rating — essentially penalizing "
"uncertainty. The wider the CI, the lower the allowable load.\n",
"\n",
"**2. When does margin of error drop below 10 units? Below 5 units?**\n"
"This depends on the standard deviation in the widget (σ ≈ 20 units by default). "
"Using ME = z* × σ/√n:\n"
"- ME < 10: √n > z* × 20/10 = 2z*; for 95% CI (z*=1.96), n > 15.4 → **n ≥ 16**\n"
"- ME < 5: n > 4 × 15.4 = 61.6 → **n ≥ 62**\n"
"Halving the margin of error requires *four times* as many measurements — a key insight "
"about diminishing returns in sampling.\n",
"\n",
"**3. Why does 99% CI produce a wider interval than 95% CI with the same data?**\n"
"To be more confident of capturing the true value, you must cast a wider net. "
"The z* multiplier increases from 1.96 (95%) to 2.576 (99%). "
"More confidence = wider interval — you cannot have both high confidence and high precision "
"without more data.\n",
"\n",
"**Common misconception:** 'A 95% CI means there's a 5% chance my interval is wrong.' "
"Partially correct — but the probabilistic statement is about the *method*, not about this "
"specific interval. Once you've computed an interval, the true value either is or isn't in it. "
"The 95% refers to the long-run performance of the method.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — St. Anthony Falls Bridge Proof Load Test\n",
"\n",
"The 2008 MnDOT proof load test is a real-world confidence interval problem: "
"engineers measured deflections at 36 sensor locations under 2 million pounds of load, "
"then compared measured results to finite element model predictions.\n",
"\n",
"**Connecting to the chapter:**\n"
"- Each deflection measurement is one draw from the population of possible measurements "
"(sensor error, load positioning variability, etc.)\n"
"- The measured mean deflection at each location gives a point estimate\n"
"- The spread across repeated load positions and sensor readings gives the uncertainty\n"
"- The confidence interval around each measurement determines whether the measured deflection "
"is statistically consistent with the model prediction\n",
"\n",
"**Why this test mattered:** The I-35W collapse (Chapter 10) had shaken public confidence "
"in bridge inspection. MnDOT needed to demonstrate — with data — that the replacement bridge "
"was behaving as modeled. Good agreement between measured and predicted deflections within "
"confidence bounds was the evidence the public needed.\n",
"\n",
"**Teaching connection:** This chapter closes the loop on Chapters 10–16. Chapter 10 showed "
"how observational studies can be confounded. Chapters 11–15 built probability tools. "
"Chapter 16 shows how confidence intervals let engineers make *formal statements of uncertainty* "
"about physical measurements — turning data into defensible engineering decisions.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. Coverage probability (warm-up):** Run Widget 2 at 95% confidence with 200 simulations. "
"Approximately how many intervals miss the true value? *(~10 out of 200.) "
"Run it again — do you get the same intervals? No — each is a fresh sample. "
"This is why 'confidence' refers to the method, not any single interval.)*\n",
"\n",
"**2. Type I and Type II errors in load rating (pair discussion):** Suppose a bridge's "
"confidence interval just barely includes a deflection that would allow a 10-ton load rating. "
"If you grant the 10-ton rating and the bridge is actually weaker (the true value falls "
"outside the interval), what happens? If you deny the 10-ton rating and the bridge is "
"actually fine, what happens? *(Connects CI decisions to Type I/II error framing: "
"one risk is structural; the other is economic.)*\n",
"\n",
"**3. Sample size and budget (small group):** From the Stop and Think answer, cutting the "
"margin of error in half requires 4× as many sensor readings. If each reading costs $500 "
"in equipment time, how much does it cost to go from ±10 to ±5 units of precision? "
"Is that precision worth the cost for a routine inspection? For approving a new bridge?\n",
"\n",
"**4. Extension (homework):** Find a news article that reports a poll result with a margin "
"of error. Write one paragraph explaining: (a) what the margin of error means, "
"(b) what confidence level was likely used, and (c) what sample size would be needed "
"to cut the margin of error in half.\n",
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
        elif cid == "reflect":
            result.append(EDU_ANSWER_KEY)
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_16_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
