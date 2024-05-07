import timeit
import matplotlib.pyplot as plt
import numpy as np

from native import naive_string_matching
from rabin_karp import rabin_karp
from finite_automaton import finite_automaton
from knuth_morris_pratt import knuth_morris_pratt

input_sizes = [10, 100, 200, 500, 1000]

algorithms = {
    "Native": naive_string_matching,
    "Rabin-Karp": rabin_karp,
    "Finite Automaton": finite_automaton,
    "Knuth-Morris-Pratt": knuth_morris_pratt
}

results = {algo: [] for algo in algorithms}

for size in input_sizes:
    text = "a" * size
    pattern = "a" * (size // 10)
    for algo_name, algo_func in algorithms.items():
        stmt = f"{algo_func.__name__}('{text}', '{pattern}')"
        setup = f"from __main__ import {algo_func.__name__}"
        execution_time = timeit.timeit(stmt, setup, number=10)
        results[algo_name].append(execution_time)

plt.figure(figsize=(10, 6))

for algo_name, timings in results.items():
    plt.plot(input_sizes, timings, label=algo_name)

plt.title("String Matching Algorithm Benchmark")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (s)")
plt.xscale("log")
plt.yscale("log")
plt.xticks(input_sizes, [str(size) for size in input_sizes])
plt.grid(True)
plt.legend()
plt.show()