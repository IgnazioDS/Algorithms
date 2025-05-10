"""
Concrete search algorithms + an adaptive wrapper.

Functions return the **index** of the target value or ``None`` if not found.
"""

from __future__ import annotations
from math import sqrt
from typing import Sequence, Optional

def linear_search(target: int, arr: Sequence[int]) -> Optional[int]:
    for i, val in enumerate(arr):
        if val == target:
            return i
    return None

def binary_search(target: int, arr: Sequence[int]) -> Optional[int]:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def jump_search(target: int, arr: Sequence[int]) -> Optional[int]:
    n = len(arr)
    step = int(sqrt(n)) or 1
    prev = 0
    while prev < n and arr[min(n - 1, prev + step - 1)] < target:
        prev += step
    for idx in range(prev, min(prev + step, n)):
        if arr[idx] == target:
            return idx
    return None

def exponential_search(target: int, arr: Sequence[int]) -> Optional[int]:
    if not arr:
        return None
    if arr[0] == target:
        return 0
    bound = 1
    n = len(arr)
    while bound < n and arr[bound] < target:
        bound *= 2
    lo, hi = bound // 2, min(bound, n - 1)
    sub_idx = binary_search(target, arr[lo:hi + 1])
    return lo + sub_idx if sub_idx is not None else None

def _is_sorted(arr: Sequence[int], probes: int = 10) -> bool:
    if len(arr) < 2:
        return True
    import random
    for _ in range(min(probes, len(arr) - 1)):
        i = random.randint(0, len(arr) - 2)
        if arr[i] > arr[i + 1]:
            return False
    return True

def adaptive_search(target: int, arr: Sequence[int], assume_sorted: Optional[bool] = None) -> Optional[int]:
    n = len(arr)
    if assume_sorted is None:
        assume_sorted = _is_sorted(arr)

    if not assume_sorted:
        if n < 1_000:
            return linear_search(target, arr)
        sorted_copy = sorted((val, idx) for idx, val in enumerate(arr))
        values = [v for v, _ in sorted_copy]
        idx_in_sorted = binary_search(target, values)
        return None if idx_in_sorted is None else sorted_copy[idx_in_sorted][1]

    if n < 32:
        return binary_search(target, arr)
    if n < 1_024:
        return jump_search(target, arr)
    return exponential_search(target, arr)
