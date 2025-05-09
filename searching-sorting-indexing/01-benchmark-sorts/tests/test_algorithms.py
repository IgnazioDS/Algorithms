import random
from benchmark_sorts import algorithms as alg

_FUNCS = [
    alg.quicksort,
    alg.mergesort,
    alg.heapsort,
    alg.timsort,
    alg.radix_sort,
]

def _random_data():
    return [random.randint(0, 1_000_000) for _ in range(1000)]

def test_correctness():
    data = _random_data()
    expected = sorted(data)
    for fn in _FUNCS:
        assert fn(data) == expected
