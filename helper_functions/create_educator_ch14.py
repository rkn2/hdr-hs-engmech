"""
Generates Chapter_14_Educator.ipynb — Educator version with answer keys and teaching notes.
Target: High school teachers (physics or statistics/math class). Basic physics assumed.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from create_ch14 import CELLS as STUDENT_CELLS

def cell(ctype, cid, source, **kw):
    base = {"cell_type": ctype, "id": cid, "metadata": {}, "source": source}
    if ctype == "code":
        base.update({"execution_count": None, "outputs": []})
    base.update(kw)
    return base

EDU_BANNER = cell("markdown", "edu_banner", [
"<div style='background:#1a1a2e;color:#eee;padding:18px;border-radius:8px;margin-bottom:12px'>\n",
"<h2 style='margin:0'>🍎 EDUCATOR VERSION — Chapter 14: Probability Rules</h2>\n",
"<p style='margin:6px 0 0'>This notebook contains answer keys, teaching notes, and discussion prompts. "
"Students should use the standard <strong>Chapter_14.ipynb</strong>.</p>\n",
"</div>\n",
])

EDU_CONTEXT = cell("markdown", "edu_context", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Context\n",
"\n",
"**Curriculum connections:**\n",
"- *Statistics class*: Conditional probability; multiplication rule for independent and "
"dependent events; addition rule (OR)\n",
"- *Physics class*: Forces and load paths in structures; what 'redundancy' means physically\n",
"\n",
"**Prerequisites:** Students should understand probability as long-run frequency and be "
"comfortable with the complement rule.\n",
"\n",
"**Estimated time:** 50–60 minutes. Spend 20 minutes on the series vs. parallel concept "
"(Widget 1) and 30 minutes on conditional probability and progressive collapse (Widget 2).\n",
"\n",
"**Sensitivity note:** The Oklahoma City bombing (1995) killed 168 people, including 19 children "
"in a daycare center. This chapter uses the Murrah Building collapse as a structural case study, "
"not a discussion of the bombing itself. Acknowledge the human context briefly and focus "
"discussion on the engineering — why the building's structural system made it so vulnerable. "
"Be aware that some students may have personal connections to this event or to domestic terrorism.\n",
"\n",
"**Pedagogical note:** The series/parallel distinction maps cleanly onto a metaphor students "
"know: a chain (series — breaks at any link) vs. a team (parallel — succeeds if anyone "
"succeeds). Use this before introducing the formulas. Widget 1 then makes the dramatic "
"difference between the two systems quantitatively visible.\n",
"</div>\n",
])

EDU_ANSWER_KEY_1 = cell("markdown", "edu_ak1", [
"<div style='background:#d4edda;padding:15px;border-left:5px solid #28a745;margin:10px 0'>\n",
"\n",
"### ✅ Answer Key — Stop and Think (Widget 1)\n",
"\n",
"**1. Series vs. parallel with 10 members at p = 0.5%:**\n"
"- Series: P(system fails) = 1 − (1 − 0.005)^10 ≈ **4.9%**\n"
"- Parallel: P(system fails) = (0.005)^10 ≈ **9.8 × 10⁻²³** (essentially zero)\n"
"The parallel system is astronomically more reliable.\n",
"\n",
"**2. Why does adding members make series *worse* and parallel *better*?** In a series system, "
"each new member is another potential failure point — one more way the chain can break. "
"In a parallel system, each new member is another backup — one more chance that *someone* "
"survives. The direction of improvement reverses.\n",
"\n",
"**3. Real-world implication:** Statically determinate trusses (series systems) are simpler to "
"analyze but have zero tolerance for member failure. Redundant frames and cable-stayed bridges "
"(parallel systems) are more complex to design but vastly more forgiving. Modern codes require "
"redundancy precisely because the parallel-system math makes it so effective.\n",
"</div>\n",
])

EDU_CASE_NOTE = cell("markdown", "edu_case_note", [
"<div style='background:#fff3cd;padding:15px;border-left:5px solid #ffc107;margin:10px 0'>\n",
"\n",
"### 🍎 Teaching Note — Alfred P. Murrah Building Case Study\n",
"\n",
"The Murrah Building used a structural system with very large column spacing and a massive "
"transfer girder at the third floor to bridge those spans. This is efficient and economical "
"in normal conditions — but it created a non-redundant load path: if the transfer girder lost "
"its support, there was no alternative.\n",
"\n",
"**Key structural point:** The transfer girder was effectively a single critical link — "
"a series connection between the columns below and the floors above. When three ground-floor "
"columns were destroyed by the blast, the girder lost support and failed, triggering "
"floor-by-floor collapse.\n",
"\n",
"**Connecting to the math:**\n",
"- P(floor fails | transfer girder has failed) ≈ 1.0 (no alternative load path)\n",
"- If there had been *multiple* transfer paths, P(floor fails | one girder fails) would be "
"much smaller — conditional probability kept low by redundancy\n",
"\n",
"**The code response:** After the Murrah collapse, GSA and DoD developed explicit "
"'alternate path' requirements: engineers must show that losing any one primary member "
"does not cause more than a limited zone of collapse. This is the parallel-system principle "
"written into law.\n",
"\n",
"**Framing for students:** The engineers did not make a calculation error. The building met "
"its design requirements. The failure was in the *requirement itself* — no code at the time "
"required the building to survive loss of multiple ground-floor columns. The bombing changed that.\n",
"</div>\n",
])

EDU_DISCUSSION = cell("markdown", "edu_discussion", [
"<div style='background:#d1ecf1;padding:15px;border-left:5px solid #17a2b8;margin:10px 0'>\n",
"\n",
"### 💬 Discussion Prompts\n",
"\n",
"**1. Series and parallel in everyday life (warm-up):** Identify one example of a series system "
"and one example of a parallel system from daily life (not structural). "
"*(Examples: series — old-style holiday light strings (one burns out, all go dark); "
"parallel — multiple lanes on a highway, duplicate hard drives in a RAID storage system.)*\n",
"\n",
"**2. The internet as a parallel system (pair discussion):** The internet was originally "
"designed by DARPA to survive nuclear attack by routing around destroyed nodes. "
"How does this relate to the probability rules from Widget 1? "
"What makes some internet outages still possible despite this design? "
"*(Guide toward: the backbone may have single-path bottlenecks; undersea cables; "
"central DNS servers — local series connections within the larger parallel network.)*\n",
"\n",
"**3. Progressive collapse in other domains (small group):** Progressive collapse isn't just "
"structural — it appears in financial crises (one bank fails, others face higher borrowing costs, "
"another fails...) and ecological cascades (one species collapses, prey populations explode, "
"another predator starves...). Identify the conditional probability logic in one of these: "
"which event is A, which is B, why is P(B|A) >> P(B)?\n",
"\n",
"**4. Extension (homework):** Research 'alternate path method' in structural engineering. "
"Find one modern building that uses it (post-Murrah or post-9/11 designs often cite it). "
"Write one paragraph explaining what structural feature provides the alternate path "
"and which load case it protects against.\n",
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
    out = os.path.join(os.path.dirname(__file__), "..", "Chapter_14_Educator.ipynb")
    with open(out, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Written → {os.path.abspath(out)}")

if __name__ == "__main__":
    build_notebook()
