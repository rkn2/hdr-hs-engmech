"""
Generates Chapter_13_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch13 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 13: Probability</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_13.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Long-run frequency interpretation of probability; geometric distribution "
"(time until first event); complement rule; independent events\n",
"- *Math class*: Exponential functions; limit of (1 − 1/n)ⁿ → 1/e as n → ∞\n",
"- *Physics class*: Measurement uncertainty over time; return period as engineering design parameter\n",
"\n",
"**Prerequisites:** Students should be comfortable with probability as long-run frequency and "
"understand the multiplication rule for independent events.\n",
"\n",
"**Estimated time:** 45–55 minutes. The concept of return period takes most students 10–15 minutes "
"to internalize; budget time for the '100-year flood' misconception discussion.\n",
"\n",
"**Pedagogical note:** The '100-year flood' misconception is nearly universal among students "
"(and the general public). The most effective approach is to ask students *before* revealing "
"the formula: 'If a flood happens once every 100 years on average, and one just happened this "
"year, how long until the next one?' Most will say '100 years.' The simulation widget then shows "
"them how wrong that intuition is — floods cluster and the gaps vary wildly.\n",
"</div>\n",
])

EDU_ANSWER_KEY_1 = cell("markdown", "edu_ak1", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think\n",
"\n",
"**1. P(at least one exceedance in 50 years) for 100-year event:**\n"
"P = 1 − (1 − 1/100)^50 = 1 − (0.99)^50 ≈ 1 − 0.605 = **39.5%**. "
"Many students are surprised it's nearly 40%. The bridge has almost a coin-flip chance of "
"experiencing its design load event over its service life.\n",
"\n",
"**2. What does '100-year event' actually mean?** It means there is a 1% chance of the event "
"occurring in any single year — not that it happens exactly once per century. Two 100-year floods "
"can happen in consecutive years. The name is misleading; engineers increasingly prefer "
"'1%-annual-chance event.'\n",
"\n",
"**3. Why the AASHTO 75-year design life and 75-year return period?** The 75-year match is "
"deliberate: P = 1 − (1 − 1/75)^75 ≈ 63%. The bridge will probably see its design load "
"at least once. But the load *factors* (1.75× live load in AASHTO LRFD) provide the margin — "
"the structure is designed to survive loads well above its nominal design value.\n",
"\n",
"**Common student error:** Thinking that a higher return period always means a safer design. "
"A 475-year earthquake design is not necessarily 'safer' than a 100-year flood design — "
"it depends on the consequences of failure and the load factors applied.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — AASHTO Bridge Design Case Study\n",
"\n",
"The AASHTO 75-year return period is one of the clearest examples of *engineering code as "
"probability statement*. Students sometimes think codes are arbitrary rules passed down by "
"authority — this case study shows the opposite: a specific probability calculation drove "
"the specification.\n",
"\n",
"**The math behind the code:**\n",
"- Design life = 75 years (standard highway bridge service life)\n",
"- Target: the nominal design load should be the load with a 1-in-75 annual probability\n",
"- P(exceeded at least once) = 1 − (1 − 1/75)^75 ≈ 63%\n",
"\n",
"**Why accept 63% probability of exceedance?** Because the bridge is not designed to fail "
"when the nominal load is exceeded — it is designed to *not fail* when the factored load "
"(1.75 × nominal for truck live load) is reached. The probability of the factored load "
"being exceeded in 75 years is much smaller.\n",
"\n",
"**Connection to the memoryless property:** The geometric distribution that describes "
"'time until first exceedance' is memoryless — a bridge that has already served 30 years "
"without seeing a 75-year event does not have a reduced probability of seeing one in the "
"next year. Each year is an independent trial. This is counterintuitive but important.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. The '500-year flood' (warm-up):** In 2015, South Carolina experienced what officials called "
"a '1000-year rain event.' The previous year, the same area had a '500-year flood.' "
"Is this statistically impossible? *(No — each year is independent. Rare events can cluster. "
"The labels reflect annual probability, not spacing.)*\n",
"\n",
"**2. Acceptable risk (pair discussion):** ASCE 7-10 uses a 2%-in-50-years earthquake "
"(2475-year return period) for the design earthquake in the US. Is a 2% chance of being "
"shaken that hard over 50 years 'acceptable'? Who decides what level of risk is acceptable? "
"*(Guide toward: engineers, building codes, insurance actuaries, elected officials, and "
"ultimately society set these thresholds — it's partly technical, partly political.)*\n",
"\n",
"**3. Design life choices (small group):** A nuclear waste storage facility is designed for "
"10,000 years. A temporary construction bridge is designed for 5 years. "
"How does design life change what return period you should use? "
"Draw a sketch of P(exceedance) vs. design life for a few return periods "
"and discuss what the curves imply.\n",
"\n",
"**4. Extension (homework):** Look up the '100-year floodplain' designation used by FEMA "
"for flood insurance purposes. What annual probability does this represent? "
"If a house is in the 100-year floodplain and you live there for 30 years, "
"what is the probability your house floods at least once? Show the calculation.\n",
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_13_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
