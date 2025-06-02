# 🧭 TSP-Problem

![GitHub Repo stars](https://img.shields.io/github/stars/radyalz/TSP-Problem?style=social)
![GitHub forks](https://img.shields.io/github/forks/radyalz/TSP-Problem?style=social)
![GitHub issues](https://img.shields.io/github/issues/radyalz/TSP-Problem)
![GitHub pull requests](https://img.shields.io/github/issues-pr/radyalz/TSP-Problem)
![GitHub last commit](https://img.shields.io/github/last-commit/radyalz/TSP-Problem)
![GitHub license](https://img.shields.io/github/license/radyalz/TSP-Problem)
![GitHub language top](https://img.shields.io/github/languages/top/radyalz/TSP-Problem)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/radyalz/TSP-Problem/ci.yml?label=CI&logo=github)

---

Welcome to an in-depth research project on the **Traveling Salesman Problem (TSP)** — a classic optimization challenge in computer science, operations research, and artificial intelligence.

This repo explores various algorithms, implementations, visualizations, and use-cases related to solving the TSP efficiently.

---

## 🧾 Contents

- 📚 [Reading List](./MarkDowns/To-Read.md) — curated research papers, articles, and learning resources.
- 🗂️ [PDF Folders](./Pdfs) — in-depth ChatGPT searches summarizing what I’ve learned so far.
- 📊 [Overview of TSP Problem (My Understanding)](./MarkDowns/ExplanationTSPProblem-no1.md) — a personal explanation of the Traveling Salesman Problem.
- 📊 [About PowerPoint](./MarkDowns/About-PowerPoint.md) — font requirements, slide formatting, and visual design tips.
- 🐍 [Python Code](./Code/Python/) — comparison of 4 popular algorithms: brute force, genetic, nearest neighbor, and 2-opt.
- 🛠️ [MATLAB Code](./Code/example.m) — coming soon!

---

## 💻 Code Usage

The Python code includes implementations of four popular TSP algorithms:

- Brute Force
- Genetic Algorithm
- Nearest Neighbor
- 2-Opt Optimization

To run the code smoothly:

1. Navigate to the `Code/Python/` folder.
2. Run the `run.bat` batch file to automatically install the required Python dependencies listed in `requirements.txt`.
3. After installation, `run.bat` will execute the main script `run_project.py` which runs and compares all four algorithms.

This setup makes it easy to get started without manually installing packages or running individual scripts.

---

## 🧑‍💼 Author

> Maintained with 🧠 and ☕ by **[radyalz](https://github.com/radyalz)**

Feel free to connect, fork, or contribute ideas!

---

## 🛠 Suggestions / Contributions

Want to suggest an algorithm, a resource, or fix a typo? Open an issue or a pull request:

- 🔧 [Create an Issue](https://github.com/radyalz/TSP-Problem/issues)
- 🔄 [Make a Pull Request](https://github.com/radyalz/TSP-Problem/pulls)

> 🙌 Contributions of all kinds are welcome — whether it's adding research, code, or just fixing typos!

### ⚠️ Issues

- 🇬🇧 There’s no English version of the lecture (PowerPoint file in the PowerPoint folder).
- 🐢 No progress in MATLAB yet because I’m still getting comfortable with it. 😊
- 🐍 I need to double-check all the Python algorithms — I was in a hurry and might have made some mistakes.
- 📄 The explanations in the markdown need more work — it’s not the best overview I’ve done. The in-depth ChatGPT search seems better. Both PDFs cover good talking points.

---

## ⭐️ Favorite This Project

If you find this useful or interesting, please give it a ⭐️ on GitHub. It helps the project grow and reach more learners!

---

## 🧪 Coming Soon

- 🧠 Visualizations using MATLAB and NetworkX
- 📈 Expanding upon the existing Python code
- 🌐 Interactive GitHub Pages demo (if applicable)

---

## 🗂 Folder Structure

```bash
└── 📁TSP-Problem
    └── 📁Code
        └── example.m
        └── 📁Python
            └── requirements.txt
            └── run_project.py
            └── run.bat
            └── tsp_compare.py
            └── 📁tsp_env
                └── basically a virtual env for python
    └── 📁MarkDowns
        └── About-PowerPoint.md
        └── ExplanationTSPProblem-no1.md
        └── To-Read.md
        └── tsp_overview.md
    └── 📁Pdfs
        └── The Traveling Salesman Problem (TSP)_ Theory, Algorithms, and Applications.pdf
        └── Traveling Salesman Problem (TSP)_ Foundations and Methods.pdf
    └── 📁PowerPoint
        └── 📁Images
            └── 1_QdxLD95imf8VnrL5nlFHdQ.gif
            └── 6n-graf.svg.png
            └── Directed_graph_no_background.svg
            └── Hamiltonian.png
            └── Jogo_icosiano_01.jpg
            └── Nearestneighbor.gif
            └── Tehranshomallogo.png
            └── Thomas_P_Kirkman.jpg
            └── Weighted_K4.svg
            └── William_Rowan_Hamilton_painting.jpg
        └── TSP Problem By Radyalz.pptx
    └── LICENSE
    └── README.md
```
