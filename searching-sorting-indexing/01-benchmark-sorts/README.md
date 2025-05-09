# 01‑benchmark‑sorts

A micro‑benchmark suite comparing classic sorting algorithms in pure Python.

## Algorithms included

| Name        | Approach              | Avg‑case time |
|-------------|-----------------------|---------------|
| quicksort   | divide & conquer      | O(n log n)    |
| mergesort   | divide & conquer      | O(n log n)    |
| heapsort    | heap selection        | O(n log n)    |
| timsort     | hybrid (Python built‑in) | O(n log n) |
| radix sort  | counting per digit (integers only) | O(k·n) |

## Running benchmarks

```bash
# From repo root
python -m benchmark_sorts.benchmark 1000 5000 20000 > results.csv
```

The script prints CSV with columns **algorithm**, **n**, **seconds**.

## Running tests

```bash
pytest
```

## Extending

* Add more algorithms in `benchmark_sorts/algorithms.py`.
* Adjust the list inside `benchmark_sorts/benchmark.py`.
* Use the generated CSV with pandas or Excel to plot results.
