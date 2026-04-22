"""
Generates Chapter_12_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch12 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 12: Counting Principles</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_12.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Multiplication counting principle; combinations vs. permutations; "
"sample space enumeration\n",
"- *Math/precalculus class*: Combinations C(n,k); factorial notation; systematic enumeration\n",
"- *Physics class*: Forces as vectors with direction — why load combinations matter physically\n",
"\n",
"**Prerequisites:** Students should be comfortable with basic multiplication and have seen "
"factorial notation. No prior knowledge of structural loads is assumed.\n",
"\n",
"**Estimated time:** 45–50 minutes. The load combination widget (Widget 1) works well as a "
"whole-class demo. Widget 2 (truss member inspection schedules) is best as independent or "
"pair work.\n",
"\n",
"**Pedagogical note:** The key insight is that combining loads is *not* just addition — "
"loads can act simultaneously in ways that create worse conditions than any single load alone. "
"The ASCE 7 load combinations encode decades of engineering judgment about which combinations "
"are credibly simultaneous. The Hartford collapse is compelling precisely because it looks obvious "
"in hindsight: snow + self-weight + vibration. Ask students: which combination would *you* have "
"checked if you'd been the engineer?\n",
"</div>\n",
])

EDU_ANSWER_KEY_1 = cell("markdown", "edu_ak1", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think\n",
"\n",
"**1. Most critical combination:** For a typical office building with moderate wind and snow, "
"ASCE 7 Combination 3 (1.2D + 1.6S + ...) or Combination 4 (1.2D + 1.6W + ...) is often "
"governing. The answer depends on which loads are largest. Students should observe from the "
"bar chart which combination produces the highest total factored load.\n",
"\n",
"**2. Why are load factors > 1.0?** Because the nominal load values (D, L, S, W...) are "
"*best estimates*, not worst-case values. The factors (1.2, 1.6, etc.) account for the "
"uncertainty that actual loads may exceed their nominal values. Dead loads (D) get factor 1.2 "
"because they're well-known; live loads (L) and wind (W) get 1.6 because they're more variable.\n",
"\n",
"**3. Why not just check the largest single load?** Because two moderate loads acting simultaneously "
"can exceed one large load acting alone. The student's own calculation from the widget should "
"show this: the governing combination is almost never the one with the single highest load.\n",
"\n",
"**Common student error:** Treating load *combinations* as load *additions* without the factors "
"(i.e., just D+L+S+W). The factors are the whole point — they transform characteristic loads "
"into design loads with an appropriate margin.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — Hartford Civic Center Case Study\n",
"\n",
"The Hartford Civic Center roof collapse (1978) is a textbook case of *missed combination*. "
"The space truss roof was designed in the early 1970s, before the widespread adoption of "
"computer-aided structural analysis. The design engineers checked gravity loads and snow loads "
"separately — but the combination of:\n",
"1. Higher-than-expected self-weight (original estimates were low)\n",
"2. Accumulated wet snow (the storm the night of collapse)\n",
"3. Vibration from HVAC equipment and crowd loads\n",
"\n",
"...exceeded the capacity of the slender compression members in the top chord.\n",
"\n",
"**Key point for students:** No individual load caused the collapse. The failure was combinatorial "
"— it required several loads to act together. This is exactly the problem the ASCE 7 load "
"combination table was designed to force engineers to check systematically.\n",
"\n",
"**Fortunate timing:** The roof collapsed at 4:19 AM, hours after a UConn basketball game that "
"had drawn 5,000 spectators. Had it collapsed during the game, casualties would have been severe.\n",
"\n",
"**Physics connection:** The failure was buckling of slender compression members (Euler buckling: "
"P_cr = π²EI/L²). The members were undersized for the actual combined load. Ask students: "
"if a column's buckling load is 80 kips, and the combined factored load reaches 95 kips, "
"what happens?\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. Combinations in daily life (warm-up):** A restaurant has 4 appetizers, 6 entrées, and "
"3 desserts. How many distinct meals can you order (one of each)? Now: what if you only want "
"2 of the 3 courses — how many options? *(The multiplication principle and combinations apply "
"directly. This bridges the abstract math to something familiar before the structural context.)*\n",
"\n",
"**2. Why factors differ (pair discussion):** Why does dead load get a factor of 1.2 but "
"live load gets 1.6? What does it mean that we're *less* certain about live loads than dead loads? "
"*(Dead load = weight of the structure itself, which is calculated from drawings and material "
"densities — well-controlled. Live load = people, furniture, stored goods — highly variable "
"and unpredictable.)*\n",
"\n",
"**3. Missed combinations (small group):** The Hartford engineers didn't use the systematic "
"combination checking that is now required. What organizational or cultural factors might "
"lead a team to skip some combinations? *(Guide toward: time pressure, overconfidence, "
"missing software, lack of peer review, assumption that 'it has always worked this way.')*\n",
"\n",
"**4. Extension (homework):** Research the term 'system safety' and find one example of a "
"multi-factor failure — in aviation, medicine, or nuclear power — where no single cause "
"was sufficient to produce the accident. Write one paragraph explaining which factors combined "
"to cause the failure.\n",
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_12_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
