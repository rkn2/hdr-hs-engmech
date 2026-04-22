"""
Generates Chapter_10_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch10 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 10: Observational Studies</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_10.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *AP Statistics*: Unit 2 (Exploring Two-Variable Data — correlation, scatter plots); "
"Unit 3 (Collecting Data — observational studies vs. experiments, confounding)\n",
"- *AP Physics*: Experimental design; controlling variables; sources of measurement error\n",
"- *Statistics / Math class*: Correlation, causation, lurking variables\n",
"\n",
"**Prerequisites:** Students should understand correlation (r), scatter plots, and basic "
"experimental design vocabulary (treatment group, control group, explanatory variable, response variable).\n",
"\n",
"**Estimated time:** 50 minutes. Can split Widget 1 + reflection (25 min) and case study + Widget 2 (25 min) "
"across two class periods.\n",
"\n",
"**Pedagogical note:** This chapter deliberately uses structural engineering to make confounding "
"*physical* rather than abstract. Students feel the intuition — *of course* traffic makes the bridge deflect! "
"— which makes the temperature-as-confound reveal more satisfying. The I-35W collapse is emotionally "
"anchored (many students have seen the footage online) and reinforces that these are not toy examples.\n",
"</div>\n",
])

EDU_ANSWER_KEY_1 = cell("markdown", "edu_ak1", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think\n",
"\n",
"**1. Before controlling for temperature:** The raw correlation between traffic and deflection is "
"approximately *r* ≈ 0.85 — very strong. An engineer would reasonably conclude that heavy traffic "
"causes high deflection. This is partially correct (traffic *does* apply load), but the correlation "
"is inflated because temperature is hidden in the background.\n",
"\n",
"**2. After controlling for temperature:** The partial correlation drops to approximately *r* ≈ 0.35–0.45. "
"Temperature was confounding both variables: warm days bring more commuters (higher traffic) AND "
"cause thermal expansion of the bridge deck (higher deflection). "
"Once temperature is accounted for, the traffic-deflection relationship is weaker and more honest. "
"The actual cause of high deflection on hot days is a *combination* of traffic load and thermal expansion — "
"not traffic alone.\n",
"\n",
"**3. Student answers vary.** Strong examples for full credit:\n",
"- Bridge age and number of reported cracks — both are driven by cumulative traffic volume and maintenance "
"budget, not by age alone (a well-maintained 50-year-old bridge may have fewer cracks than a neglected 20-year-old one)\n",
"- Column height and foundation cost — both correlate with building size (footprint), not with each other directly\n",
"- Ice cream sales and drowning rates — both driven by heat/summer season (classic lurking variable example)\n",
"- Concrete strength and curing temperature — both are affected by mix design and climate\n",
"\n",
"**Common student error:** Confusing the *direction* of confounding (thinking the confound makes "
"the correlation look weaker, not stronger). Emphasize: confounders typically inflate correlations "
"by creating a backdoor path between the two variables.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — I-35W Case Study\n",
"\n",
"The gusset plate failure is a textbook confounding case: inspection reports noted cracking in high-stress "
"zones (the outcome), but the explanatory variable (gusset plate overload) was misidentified. "
"Engineers attributed the cracks to surface corrosion from weather — not structural overstress. "
"This is the correlation-vs-causation problem applied to real engineering judgment.\n",
"\n",
"**Key point for students:** The failure was not due to negligence or incompetence. The inspectors "
"correctly observed the data (cracks exist). The error was in the *causal inference* — assuming "
"weathering caused the cracks rather than asking whether stress could also explain them. "
"This is why formal confounding analysis matters even for experienced engineers.\n",
"\n",
"**Physics connection:** The gusset plates were calculated to handle a certain stress (σ = F/A). "
"Because the plates were undersized *from original design*, the actual stress had been above the "
"design allowable for decades. The added construction equipment (570,000 lbs) on the day of collapse "
"was the proximate cause, but the design error was the root cause.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. Medical analogy (5 min):** In the 1950s, observational studies found that coffee drinkers had "
"higher rates of lung cancer. Coffee appeared to *cause* cancer. What was the confounding variable? "
"*(Answer: smoking — coffee drinkers at that time were more likely to smoke. Coffee and lung cancer "
"were both correlated with smoking, not with each other.)* How does this parallel the bridge sensor scenario?\n",
"\n",
"**2. Inspection failure (pair discussion):** The I-35W bridge was inspected regularly for 40 years. "
"Why didn't those inspections catch the gusset plate problem? "
"What would a better inspection protocol have looked like? "
"*(Guide toward: inspections were visual; gusset plates were covered by other structural elements; "
"inspectors lacked a model predicting which zones were overstressed.)*\n",
"\n",
"**3. Sensor design (small group):** Engineers monitor real bridges with continuous sensor networks "
"(structural health monitoring). If you were designing a monitoring system for a bridge in a climate "
"with large temperature swings, what variables would you measure to avoid the confounding problem "
"shown in Widget 1? *(Students should identify: temperature, traffic count AND weight, humidity, "
"solar radiation — anything that independently affects deflection.)*\n",
"\n",
"**4. Extension (homework):** Research the difference between observational studies and randomized "
"controlled trials in medicine. Find one example where an observational study suggested a causal "
"relationship that an RCT later reversed. *(Classic examples: hormone replacement therapy and heart disease; "
"beta-carotene and cancer prevention.)* Write one paragraph explaining what the confounding variable was.\n",
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
        elif cid == "reflect1":
            result.append(EDU_ANSWER_KEY_1)
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_10_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
