"""CLI benchmarking harness.

Usage:
    python -m benchmark_sorts.benchmark 1000 5000 20000
This will benchmark each algorithm on arrays of 1000, 5000, 20000 random ints
and output CSV to stdout.

You can redirect to a file:
    python -m benchmark_sorts.benchmark 1000 5000 > results.csv
"""

import random, time, sys, csv
from typing import List, Callable
from . import algorithms as alg

ALGOS: dict[str, Callable[[List[int]], List[int]]] = {
    "quicksort": alg.quicksort,
    "mergesort": alg.mergesort,
    "heapsort":  alg.heapsort,
    "timsort":   alg.timsort,
    "radix_sort": alg.radix_sort,
}

def benchmark_one(func: Callable[[List[int]], List[int]], data: List[int]) -> float:
    start = time.perf_counter()
    _ = func(data)
    return time.perf_counter() - start

def run(n_values: List[int], trials: int = 5) -> List[tuple]:
    results = []
    for n in n_values:
        base = [random.randint(0, 10_000_000) for _ in range(n)]
        for name, fn in ALGOS.items():
            # One warm‑up run
            fn(base)
            times = [benchmark_one(fn, base) for _ in range(trials)]
            avg = sum(times) / trials
            results.append((name, n, avg))
    return results

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m benchmark_sorts.benchmark n1 n2 ...", file=sys.stderr)
        sys.exit(1)
    sizes = [int(x) for x in sys.argv[1:]]
    writer = csv.writer(sys.stdout)
    writer.writerow(["algorithm", "n", "seconds"])
    for row in run(sizes):
        writer.writerow(row)

if __name__ == "__main__":
    main()
