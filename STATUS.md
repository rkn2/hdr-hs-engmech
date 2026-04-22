# Project Status — HDR High School Engineering Mechanics

_Last updated: 2026-04-21_

## What This Project Is

Interactive Jupyter notebooks (Chapters 9–16) teaching statistics through structural engineering.
Each chapter pairs a core statistics concept with a real engineering context, two interactive widgets,
and a real-world case study. Designed for high school students; generated from Python scripts in
`helper_functions/`.

---

## Current State

### Student Notebooks ✅ Complete

All notebooks have been updated with:
- Opening photos (public domain / Wikimedia Commons)
- Real engineering case studies (see list below)
- Refined widget content and illustrative-value disclosures
- Hibbeler textbook references noted as context (students do not have the book)

| Chapter | Topic | Case Study |
|---------|-------|------------|
| Ch 9 | Samples & Surveys | — |
| Ch 10 | Observational Studies | I-35W Minneapolis collapse (2007) |
| Ch 11 | Randomness | Quebec Bridge collapse (1907); ASTM C39 concrete cylinder tests |
| Ch 12 | Counting Principles | Hartford Civic Center roof collapse (1978) |
| Ch 13 | Probability | AASHTO 75-year bridge live load return period |
| Ch 14 | Probability Rules | Alfred P. Murrah Building, Oklahoma City (1995) |
| Ch 15 | Probability Models | LRFD vs. ASD calibration; reliability index β = 3.5 |
| Ch 16 | Confidence Intervals | St. Anthony Falls Bridge proof load test (2008) |

### Educator Notebooks ✅ Complete

Parallel educator versions exist for Ch 10–16 (`Chapter_XX_Educator.ipynb`), generated from
`helper_functions/create_educator_chXX.py`. Each educator notebook includes:

- **Dark banner** identifying it as educator-only
- **Teaching context** (yellow) — curriculum connections to stats/physics/math classes, prerequisites, timing, pedagogical notes
- **Answer keys** (green) — worked answers for all Stop and Think questions
- **Teaching notes** (yellow) — case study framing, physics connections, emotional/historical context
- **Discussion prompts** (blue) — 4 prompts per chapter (warm-up, pair, small group, homework extension)

Educator notebooks are curriculum-neutral — no specific course or exam framework is referenced.

---

## What Still Needs to Be Done

### High Priority

- [ ] **Verify photo URLs load in Colab.** Several Wikimedia URLs were best-effort guesses.
  Test each chapter's opening image in a live Colab session. Known uncertain URLs:
  - Ch 11: concrete cylinder testing machine (`Compressive_strength_testing_machine.jpg`)
  - Ch 12: Hartford Civic Center (`Hartford_Civic_Center_Coliseum.jpg`)
  - Ch 14: Murrah Building FEMA photo (`Oklahoma_City_Bombing_FEMA.jpg`)
  - Ch 15: structural lab beam test (`Beam_bending_test.jpg`)
  - Ch 16 / Ch 13: St. Anthony Falls Bridge (same URL, more likely to be correct)

- [ ] **Chapter 9 educator version.** Ch 9 (Samples & Surveys) has no educator notebook yet.
  If educator versions are needed for the full set, Ch 9 needs its own `create_educator_ch9.py`.

- [ ] **Update README Colab links** to include all educator notebooks (Ch 10–16 educator versions
  are not yet linked in README.md).

### Lower Priority

- [ ] **Review widget answer keys for Ch 11 placement.** The Ch 11 educator notebook injects
  Widget 1 answer key after the case study (not after the widget itself, since Ch 11 has no
  reflect cells). Consider adding `reflect1`/`reflect2` stop-and-think markdown cells to
  `create_ch11.py` so the answer key injection point is more natural.

- [ ] **Ch 10 educator — answer key for question 3** mentions specific examples (ice cream/drowning,
  column height/foundation cost). Confirm these are appropriate for the target audience.

- [ ] **Colab compatibility check.** Run each notebook end-to-end in Colab to confirm widgets
  render correctly with `ipywidgets` and `%matplotlib inline`.

---

## File Structure

```
engineering_mechanics/
├── Chapter_9.ipynb               # student
├── Chapter_10.ipynb – Chapter_16.ipynb   # student (all updated)
├── Chapter_10_Educator.ipynb – Chapter_16_Educator.ipynb  # educator
├── helper_functions/
│   ├── create_ch9.py – create_ch16.py    # student notebook generators
│   └── create_educator_ch10.py – create_educator_ch16.py  # educator generators
├── README.md
└── STATUS.md                     # this file
```

To regenerate all notebooks after editing a generator script:

```bash
# Student notebooks
for ch in 9 10 11 12 13 14 15 16; do python3 helper_functions/create_ch${ch}.py; done

# Educator notebooks
for ch in 10 11 12 13 14 15 16; do python3 helper_functions/create_educator_ch${ch}.py; done
```
