"""
Mini CLI demo for adaptive_search.

Usage:
    python -m adaptive_search.cli <value> <length> [--sorted]

Example:
    python -m adaptive_search.cli 42 1000 --sorted
"""
import argparse, random, sys
from . import adaptive_search

def build_array(length: int, is_sorted: bool) -> list[int]:
    arr = [random.randint(0, 1_000_000) for _ in range(length)]
    if is_sorted:
        arr.sort()
    return arr

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=int, help="target value to search for")
    parser.add_argument("length", type=int, help="length of random array")
    parser.add_argument("--sorted", action="store_true", help="pre-sort the array")
    args = parser.parse_args()

    arr = build_array(args.length, args.sorted)
    idx = adaptive_search(args.value, arr, assume_sorted=args.sorted if args.sorted else None)
    if idx is None:
        print("Value not found")
        sys.exit(1)
    print(f"Found at index {idx}")

if __name__ == "__main__":
    main()
