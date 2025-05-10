# 02-adaptive-search

A single API that chooses the most appropriate search algorithm (linear, binary, jump, or exponential) at runtime based on:

* array length
* whether the array is already sorted (detected heuristically or told by caller)

The goal is to demonstrate **algorithm-selection in practice**—showing that no one search technique dominates across every workload.

## Quick start

```bash
# install test requirements
pip install -r requirements.txt

# run unit tests
pytest

# small demo
python -m adaptive_search.cli 42 20        # searches the value 42 in an array of length 20
```

## Files

```
src/adaptive_search/
    __init__.py        # public API
    searchers.py       # concrete search implementations
    cli.py             # example command-line interface
tests/
    test_adaptive_search.py
```

## Complexity

| Algorithm         | Time complexity | When it’s chosen                       |
|-------------------|-----------------|----------------------------------------|
| Linear search     | **O(n)**        | Small arrays or unsorted data          |
| Binary search     | **O(log n)**    | Sorted arrays, small/medium sizes      |
| Jump search       | **O(√n)**       | Sorted arrays, medium sizes            |
| Exponential + bin | **O(log n)**    | Sorted arrays, large sizes             |
