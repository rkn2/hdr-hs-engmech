# HDR High School Engineering Mechanics
### Interactive Structural Analysis Notebooks for K–12 Students

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_9.ipynb)

---

## What Is This?

This repository contains interactive Jupyter Notebooks that teach **data science and statistics concepts through the lens of structural engineering** — designed for high school students with no prior engineering background.

Each notebook takes a topic from a standard high school statistics curriculum and grounds it in a real structural engineering problem, using examples drawn directly from **R. C. Hibbeler's *Structural Analysis*, 8th Edition** (Pearson Prentice Hall, 2012). Students run simulations, manipulate variables with sliders, and see how the same ideas that govern poll sampling or probability also govern whether a bridge stands or falls.

---

## Inspiration

### The Original Project
This work extends the [HDR Data Science K–12 curriculum](https://github.com/rkn2/hdr-dsc-k12), which transformed a standard high school statistics course into interactive Google Colab notebooks. That project demonstrated that students engage more deeply with statistical concepts when they can *run experiments* rather than just read about them.

### Why Hibbeler?
The original curriculum used generic, relatable examples — basketball player heights to illustrate sampling bias, pizza delivery times to explore probability. These worked, but they felt disconnected from the kind of engineering problems students might actually encounter in college or careers.

Hibbeler's *Structural Analysis* is one of the most widely used undergraduate engineering textbooks in the United States. Its examples are concrete (sometimes literally), its case studies are real, and its problems are grounded in the same ASCE/AISC codes that practicing engineers use every day. More importantly, structural engineering turns out to be a *remarkably good* vehicle for statistics education:

- **Sampling** → How do you estimate the load on 500 floor bays when you can only inspect 30?
- **Observational studies** → How did engineers learn that wind loads could destroy a bridge they thought was safe?
- **Probability** → What is the chance that a beam's actual strength falls below its design load?
- **Confidence intervals** → How much uncertainty is built into a code-specified load factor?

The goal is not to teach structural engineering. It is to show students that the statistics they are learning is the same reasoning that keeps buildings standing — and that when the reasoning fails, real consequences follow.

---

## Notebooks

All notebooks open directly in Google Colab — no download or account required beyond a Google login.

| Chapter | Topic | Structural Engineering Context | Open in Colab |
|---------|-------|-------------------------------|---------------|
| 9 | **Samples** | Estimating building loads from floor inspections; Hyatt Regency collapse | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_9.ipynb) |
| 10 | **Observational Studies** | Bridge sensor data; confounding variables; I-35W Minneapolis collapse | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_10.ipynb) |
| 11 | **Understanding Randomness** | Steel material variability (ASTM A572); Law of Large Numbers in mill testing | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_11.ipynb) |
| 12 | **Counting Principles** | ASCE 7-10 load combinations; Hartford Civic Center roof collapse | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_12.ipynb) |
| 13 | **Probability** | Return periods; annual exceedance probability; design life risk | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_13.ipynb) |
| 14 | **Probability Rules** | Series vs. parallel structural systems; progressive collapse; Ronan Point | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_14.ipynb) |
| 15 | **Probability Models** | Normal distribution of loads and resistances; LRFD reliability index β | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_15.ipynb) |
| 16 | **Confidence Intervals** | Bridge load testing; margin of error in stiffness estimates; Silver Bridge | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_16.ipynb) |

---

## Educator Notebooks

Each chapter (10–16) has a companion **Educator Notebook** intended for teachers only. These are not linked from the student-facing materials.

Each educator notebook includes:
- A dark banner marking it as educator-only
- **Teaching context** (yellow) — curriculum connections to statistics, physics, and math classes
- **Answer keys** (green) — worked solutions after Stop and Think questions and widget sections
- **Teaching notes** (yellow) — discussion guidance after case studies
- **Discussion prompts** (blue) — questions to pose before the chapter review

| Chapter | Open Educator Notebook |
|---------|----------------------|
| 10 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_10_Educator.ipynb) |
| 11 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_11_Educator.ipynb) |
| 12 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_12_Educator.ipynb) |
| 13 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_13_Educator.ipynb) |
| 14 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_14_Educator.ipynb) |
| 15 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_15_Educator.ipynb) |
| 16 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rkn2/hdr-hs-engmech/blob/main/Chapter_16_Educator.ipynb) |

---

## How the Notebooks Are Built

Each notebook is generated by a corresponding script in the [`helper_functions/`](helper_functions/) folder. To regenerate a notebook after editing its script:

```bash
python3 helper_functions/create_ch9.py          # regenerates Chapter_9.ipynb
python3 helper_functions/create_educator_ch10.py  # regenerates Chapter_10_Educator.ipynb
```

The helper scripts define every cell as a Python dictionary, making it straightforward to update text, swap examples, or adjust widget parameters without touching raw notebook JSON.

---

## Textbook Reference

> Hibbeler, R. C. (2012). *Structural Analysis* (8th ed.). Pearson Prentice Hall.
> ISBN-13: 978-0-13-257053-4

Load values, design codes, and structural examples in these notebooks are drawn from Hibbeler Chapters 1–4 and the ASCE/SEI 7-10 standard referenced throughout the text.

---

## Related Projects

- [hdr-dsc-k12](https://github.com/rkn2/hdr-dsc-k12) — the original HDR statistics curriculum that inspired this project
