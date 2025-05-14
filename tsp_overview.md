# Traveling Salesman Problem (TSP): Foundations and Methods

The **Traveling Salesman Problem (TSP)** asks: _“Given a list of cities and the distances between each pair, what is the shortest possible route that visits each city exactly once and returns to the origin?”_

![TSP Problem Illustration](https://upload.wikimedia.org/wikipedia/commons/1/15/Euclidean_tsp.svg)

In graph-theoretic terms, TSP is modeled on a **complete weighted graph**: cities are vertices, edges are possible paths with weights equal to distances or costs, and a _tour_ is a Hamiltonian cycle (visiting each vertex once and returning to start) of minimal total weight.

(If distances differ by direction, one has the _asymmetric TSP_ on a directed graph.)

TSP is **computationally intractable** in general. The decision version (“is there a tour of length ≤ L?”) is **NP-complete**, and the optimization version is **NP-hard**.

![TSP Complexity Chart](https://upload.wikimedia.org/wikipedia/commons/e/e0/Tsp-approx.png)

This means no polynomial-time algorithm is known, and the worst-case running time grows _superpolynomially_ (e.g. factorial or exponential) with the number of cities.

---

## Exact Solution Methods

- **Brute Force:** Try all _n_! permutations of cities.
- **Dynamic Programming (Held–Karp):** Solves in Θ(2^n n^2) time.
- **Branch and Bound / Branch and Cut:** Prunes poor paths and solves instances up to tens of thousands of cities using methods like Concorde.

## Approximate and Heuristic Methods

- **Nearest Neighbor, Greedy Insertion**
- **Christofides’ Algorithm** (for metric TSP): guarantees ≤1.5× optimal.

![Christofides Algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Christofides_algorithm.svg/2880px-Christofides_algorithm.svg.png)

- **2-opt, 3-opt, Lin–Kernighan (LKH)**
- **Genetic Algorithms**
- **Simulated Annealing**

![Simulated Annealing Example](https://upload.wikimedia.org/wikipedia/commons/7/72/Simulated_annealing.gif)

- **Ant Colony Optimization (ACO)**
- **Particle Swarm Optimization (PSO)**

---

## Convex-Optimization Relaxations

Integer programming relaxations can provide lower bounds for branch-and-cut methods.

---

## Real-World Applications

- Logistics and routing
- Manufacturing (PCB drilling)
- Astronomy (observatory scheduling)
- Robotics, bioinformatics, and genomics

![Robot route planning TSP](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/TSP_LKH_route.svg/1024px-TSP_LKH_route.svg.png)

---

## Variations and Related Problems

- Multiple Salesmen (mTSP), Vehicle Routing (VRP)
- Time Windows, Asymmetric TSP (ATSP)
- Bottleneck TSP, Generalized TSP

---

## Resources and Tools

- **Python:** NetworkX, OR-Tools
- **Solvers:** Concorde, LKH
- **Visualization:** pyTSP, TSPLIB instances

---

For further exploration, visit TSPLIB, or try heuristic demos online!
