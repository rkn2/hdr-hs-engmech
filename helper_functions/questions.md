# Open Questions — HDR HS Engineering Mechanics

Questions that came up during chapter development. Work through these together before finalizing.

---

## Chapter 9 (Samples)
*No blocking questions — chapter is complete.*

---

## Chapter 10 (Observational Studies)
1. **Case study choice**: I used the I-35W Minneapolis bridge collapse (2007). The original stats project used Tacoma Narrows. Should I swap in Tacoma Narrows here to maintain a consistent "famous bridge" thread across the whole curriculum, or keep I-35W since it better illustrates observational investigation vs. experiment?
2. **Confounding widget**: The temperature/traffic/deflection example is realistic but abstract for a student who hasn't seen a bridge sensor. Would a more visual diagram of the bridge with labeled sensors help, or is the scatter plot sufficient?

---

## Chapter 11 (Understanding Randomness)
3. **Steel grade**: I used ASTM A572 Grade 50. Hibbeler references this steel but doesn't give statistical distributions for it. Is it okay to use realistic but approximate values (mean ~55 ksi, SD ~3.5 ksi), or do you want to note explicitly that these are illustrative rather than from the textbook?
4. **Truck weight simulation**: The second widget uses truck weights from a log-normal-ish distribution. This drifts slightly from Hibbeler into transportation engineering. Should I replace this with a purely material-testing widget (e.g., concrete cylinder tests) to stay closer to structural analysis?

---

## Chapter 12 (Counting Principles)
5. **Load combination widget**: The widget uses approximate nominal load values (D=40k, L=20k, etc.) to show which ASCE combination governs. These are illustrative, not from a specific Hibbeler example. Should I tie them to a real Hibbeler problem (e.g., Example 1.2's two-story building) so students can verify by hand?
6. **Hartford Civic Center**: This collapse is not widely known to high school students. Would adding a one-sentence hook ("the roof collapsed just 18 hours after 5,000 fans left a basketball game") help engagement, or is the existing writeup sufficient?

---

## Chapter 13 (Probability)
7. **Return period framing**: I used flood/wind/earthquake return periods. All of these are *indirectly* in Hibbeler (§1.3 references ASCE 7-10 which uses these concepts), but Hibbeler doesn't derive them. Is that level of connection close enough, or should I find a more direct Hibbeler example?
8. **1993 Midwest Floods case study**: This is a hydrology example, not structural analysis. Should I replace it with a structural probability case (e.g., the probability argument for why AASHTO uses a 75-year return period for bridge live loads) even though it's less familiar to students?

---

## Chapter 14 (Probability Rules)
9. **Progressive collapse simulation**: The simulation uses a simplified model where failure probability doubles with each additional floor load. This is conceptually correct but not derived from any specific structural analysis. Should I add a note making this simplification explicit?
10. **Ronan Point**: This is a UK example (1968). Some students may be more engaged by a US example like the Alfred P. Murrah Federal Building bombing (1995) which also triggered progressive collapse research. Preference?

---

## Chapter 15 (Probability Models)
11. **scipy dependency**: Chapter 15 imports `scipy.stats` for normal distribution calculations. scipy is pre-installed in Colab, so this should work fine — but it's a heavier dependency than other chapters. Should I flag this in the setup cell or replace with a pure numpy implementation?
12. **LRFD load factors**: I present 1.2D + 1.6L as the key LRFD combination. This is in Hibbeler's context but he doesn't fully derive the factors. Should I add a sentence explicitly saying "these numbers come from calibration studies, not from first principles in this textbook" to avoid confusing students?
13. **β = 3.5 target**: Is this the right number to cite for a high school audience? Some sources use β = 3.0 for gravity-load-dominated design. Want to make sure the number matches what you'd reference in your courses.

---

## Chapter 16 (Confidence Intervals)
14. **EI units**: I used "×10³ kip·ft²" as the unit for flexural stiffness to keep the numbers readable. A real W18×97 beam has EI ≈ 55,000,000 kip·in² which is unwieldy for display. Is the simplified unit okay, or should I use a different beam/unit system?
15. **Silver Bridge**: Strong case study, but the connection to confidence intervals is somewhat indirect (arguing that *if* tests had been done, they *would have* shown degradation). Would a more direct example — like an actual proof load test program with published data — be better, even if less dramatic?
16. **t-distribution vs. z**: For small n (2–5 tests), the t-distribution matters a lot. For n > 30, it converges to z. Should I add a visual comparing t and z distributions, or is that level of detail beyond the high school scope?

---

## General / Cross-Chapter
17. **Hibbeler problem numbers**: Should each chapter reference a specific Hibbeler example problem (e.g., "Try Hibbeler Example 1.2 after this section")? This would make the notebooks feel more like a genuine companion to the textbook.
18. **Educator versions**: Do you want educator versions (with answer keys and discussion prompts) for any of these chapters, parallel to the EM versions in the original stats project?
19. **Visual consistency**: Each chapter has two interactive widgets and one case study. Should the chapter opening have a photograph (like Hibbeler uses) rather than just a title? If so, are there specific images you want to use or should I find public-domain options?
20. **Chapter ordering**: The current order (9–16) mirrors the original stats curriculum. Does this ordering make sense for the engineering audience, or would you rearrange (e.g., put probability models before probability rules)?
