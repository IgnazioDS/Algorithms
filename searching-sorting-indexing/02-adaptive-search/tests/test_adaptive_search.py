import random, pytest
from adaptive_search import (
    adaptive_search,
    linear_search,
    binary_search,
    jump_search,
    exponential_search,
)

_FUNCS = [linear_search, binary_search, jump_search, exponential_search, adaptive_search]

@pytest.mark.parametrize("n,sorted_flag", [(0, False), (1, False), (25, True), (1000, False), (5000, True)])
def test_all_search_variants(n, sorted_flag):
    arr = [random.randint(0, 1_000_000) for _ in range(n)]
    if sorted_flag:
        arr.sort()
    if n:
        target_idx = random.randrange(n)
        target = arr[target_idx]
        for fn in _FUNCS:
            assert fn(target, arr[:]) == target_idx
    else:
        for fn in _FUNCS:
            assert fn(42, arr) is None
