"""Classic sorting algorithms implemented in pure Python.

Each function returns a *new* sorted list, leaving input unmodified.
Runtime complexities (average‑case):
- quicksort:    O(n log n)
- mergesort:    O(n log n)
- heapsort:     O(n log n)
- timsort:      O(n log n)  (calls Python built‑in sorted)
- radix_sort:   O(k·n) for k digit passes, only for non‑negative ints
"""

from typing import List

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def heapsort(arr: List[int]) -> List[int]:
    import heapq
    heap = list(arr)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

def timsort(arr: List[int]) -> List[int]:
    return sorted(arr)

def radix_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []
    if any(x < 0 for x in arr):
        raise ValueError("radix_sort only handles non-negative integers")
    max_val = max(arr)
    exp = 1
    output = arr[:]
    while max_val // exp > 0:
        output = _counting_sort(output, exp)
        exp *= 10
    return output

def _counting_sort(arr: List[int], exp: int) -> List[int]:
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    return output
