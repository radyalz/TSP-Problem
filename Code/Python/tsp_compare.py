import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
import sys
import random
import time

NUM_CITIES = 10
cities = np.random.rand(NUM_CITIES, 2) * 100

def distance(a, b):
    return np.linalg.norm(a - b)

def total_distance(path, cities):
    return sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1)) + distance(cities[path[-1]], cities[path[0]])

def tsp_nearest_neighbor(cities):
    unvisited = list(range(len(cities)))
    path = [unvisited.pop(0)]
    attempts = 0
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda i: distance(cities[last], cities[i]))
        unvisited.remove(next_city)
        path.append(next_city)
        attempts += 1
        yield path, attempts

def tsp_brute_force(cities):
    perms = permutations(range(len(cities)))
    shortest_path = None
    min_dist = float('inf')
    attempts = 0
    for perm in perms:
        dist = total_distance(perm, cities)
        attempts += 1
        if dist < min_dist:
            min_dist = dist
            shortest_path = perm
        yield list(perm), attempts, shortest_path, min_dist

def two_opt(path, cities):
    def swap_2opt(route, i, k):
        new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
        return new_route

    path = path[:]  # copy
    improved = True
    attempts = 0
    while improved:
        improved = False
        for i in range(1, len(path) - 1):
            for k in range(i+1, len(path)):
                new_route = swap_2opt(path, i, k)
                if total_distance(new_route, cities) < total_distance(path, cities):
                    path = new_route
                    improved = True
                    attempts += 1
                    yield path, attempts
        if not improved:
            break

def genetic_algorithm(cities, population_size=20, generations=100):
    def create_route():
        route = list(range(len(cities)))
        random.shuffle(route)
        return route

    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child_p1 = parent1[start:end+1]
        child_p2 = [item for item in parent2 if item not in child_p1]
        return child_p2[:start] + child_p1 + child_p2[start:]

    def mutate(route, mutation_rate=0.1):
        for i in range(len(route)):
            if random.random() < mutation_rate:
                j = random.randint(0, len(route)-1)
                route[i], route[j] = route[j], route[i]

    population = [create_route() for _ in range(population_size)]
    attempts = 0

    for gen in range(generations):
        population = sorted(population, key=lambda r: total_distance(r, cities))
        best = population[0]
        attempts += 1
        yield best, attempts
        new_population = population[:population_size//2]

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

def plot_path(ax, cities, path, title):
    ax.clear()
    ax.set_title(title, fontsize=12)
    for i, (x, y) in enumerate(cities):
        ax.plot(x, y, 'ro')
        ax.text(x + 1, y + 1, f'{i}', fontsize=10, color='blue')
    if path:
        for i in range(len(path)):
            start = cities[path[i]]
            end = cities[path[(i + 1) % len(path)]]
            ax.plot([start[0], end[0]], [start[1], end[1]], 'g-')
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 110)
    ax.grid(True)

def on_close(event):
    print("Plot window closed, terminating the application...")
    sys.exit(0)

plt.ion()
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.canvas.mpl_connect('close_event', on_close)

explanations = [
    "Nearest Neighbor: Greedy algorithm choosing closest next city step-by-step.",
    "Brute Force: Checks every possible path to find the shortest.",
    "2-Opt: Improves a route by swapping two edges iteratively.",
    "Genetic Algorithm: Evolutionary approach using crossover and mutation."
]

nn_generator = tsp_nearest_neighbor(cities)
bf_generator = tsp_brute_force(cities)
two_opt_generator = None
ga_generator = genetic_algorithm(cities)

path_nn, nn_attempts, nn_length = [], 0, None
path_bf, bf_attempts, bf_best_path, bf_best_dist = [], 0, None, float('inf')
path_2opt, two_opt_attempts, two_opt_length = [], 0, None
path_ga, ga_attempts, ga_length = [], 0, None

two_opt_ready = False
try:
    while True:
        # Nearest Neighbor step
        try:
            path_nn, nn_attempts = next(nn_generator)
            nn_length = total_distance(path_nn, cities)
            if not two_opt_ready and len(path_nn) == NUM_CITIES:
                two_opt_generator = two_opt(path_nn, cities)
                two_opt_ready = True
        except StopIteration:
            pass

        # Brute Force step
        try:
            path_bf, bf_attempts, bf_best_path, bf_best_dist = next(bf_generator)
        except StopIteration:
            pass

        # 2-Opt step
        if two_opt_ready and two_opt_generator is not None:
            try:
                path_2opt, two_opt_attempts = next(two_opt_generator)
                two_opt_length = total_distance(path_2opt, cities)
            except StopIteration:
                pass

        # Genetic Algorithm step
        try:
            path_ga, ga_attempts = next(ga_generator)
            ga_length = total_distance(path_ga, cities)
        except StopIteration:
            pass

        # Plot Nearest Neighbor
        plot_path(
            axs[0, 0], cities, path_nn,
            f"Nearest Neighbor\nAttempts: {nn_attempts}\nCities visited: {len(path_nn)} / {NUM_CITIES}\nCurrent length: {nn_length:.2f}" if nn_length else "Nearest Neighbor"
        )
        axs[0, 0].text(0, -15, explanations[0], fontsize=9)

        # Plot Brute Force
        cities_visited_bf = len(path_bf) if path_bf else 0
        plot_path(
            axs[0, 1], cities, path_bf,
            f"Brute Force\nAttempts: {bf_attempts}\nCities visited: {cities_visited_bf} / {NUM_CITIES}\nBest distance: {bf_best_dist:.2f}" if bf_best_path else "Brute Force"
        )
        axs[0, 1].text(0, -15, explanations[1], fontsize=9)

        # Plot 2-Opt
        if path_2opt:
            plot_path(
                axs[1, 0], cities, path_2opt,
                f"2-Opt\nAttempts: {two_opt_attempts}\nCities visited: {len(path_2opt)} / {NUM_CITIES}\nCurrent length: {two_opt_length:.2f}"
            )
        else:
            axs[1, 0].clear()
            axs[1, 0].set_title("2-Opt")
        axs[1, 0].text(0, -15, explanations[2], fontsize=9)

        # Plot Genetic Algorithm
        if path_ga:
            plot_path(
                axs[1, 1], cities, path_ga,
                f"Genetic Algorithm\nAttempts: {ga_attempts}\nCities visited: {len(path_ga)} / {NUM_CITIES}\nCurrent length: {ga_length:.2f}"
            )
        else:
            axs[1, 1].clear()
            axs[1, 1].set_title("Genetic Algorithm")
        axs[1, 1].text(0, -15, explanations[3], fontsize=9)

        plt.suptitle(f"TSP Algorithm Comparison ({NUM_CITIES} Cities)", fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.pause(0.01)

except StopIteration:
    print("All iterations completed.")
    plt.ioff()
    plt.show()
