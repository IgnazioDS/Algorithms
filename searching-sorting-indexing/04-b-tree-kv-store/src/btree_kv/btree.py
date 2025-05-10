"""Simple, *educational* in‑memory B‑tree key‑value store.

The implementation follows the CLRS algorithms for search and insert.
Deletions are omitted to keep the code compact.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Any, Optional, Tuple

class BTreeKV:
    """B‑tree with fixed minimum degree *t* (default 3)."""

    @dataclass
    class _Node:
        keys: List[str] = field(default_factory=list)
        values: List[Any] = field(default_factory=list)
        children: List['BTreeKV._Node'] = field(default_factory=list)
        leaf: bool = True  # a node is leaf if it has no children

    def __init__(self, t: int = 3):
        if t < 2:
            raise ValueError("B‑tree minimum degree must be ≥ 2")
        self.t = t
        self.root: BTreeKV._Node = self._Node()

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def search(self, key: str) -> Optional[Any]:
        """Return value associated with *key* or None if absent."""
        node, idx = self._search(self.root, key)
        return None if node is None else node.values[idx]

    def set(self, key: str, value: Any) -> None:
        """Insert or overwrite *key* → *value*."""
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # root is full
            new_root = self._Node(leaf=False, children=[root])
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def items(self) -> List[Tuple[str, Any]]:
        """Return all (key, value) pairs in sorted order (for tests)."""
        result: List[Tuple[str, Any]] = []
        self._traverse(self.root, result)
        return result

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #

    def _search(self, node: _Node, key: str) -> Tuple[Optional[_Node], int]:
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        if node.leaf:
            return None, -1
        return self._search(node.children[i], key)

    def _insert_non_full(self, node: _Node, key: str, value: Any) -> None:
        i = len(node.keys) - 1
        if node.leaf:
            # Insert key into sorted position in leaf
            node.keys.append("")     # dummy to extend list
            node.values.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                node.values[i + 1] = node.values[i]
                i -= 1
            node.keys[i + 1] = key
            node.values[i + 1] = value
        else:
            # Find child to recurse into
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            # Split child if full
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                # After split, determine which of the two children we need
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def _split_child(self, parent: _Node, idx: int) -> None:
        """Split full child *parent.children[idx]* around median."""
        t = self.t
        full_child = parent.children[idx]
        new_child = self._Node(
            keys = full_child.keys[t:],           # right half keys
            values = full_child.values[t:],
            children = full_child.children[t:] if not full_child.leaf else [],
            leaf = full_child.leaf
        )
        # Median key/value to push up
        median_key = full_child.keys[t - 1]
        median_val = full_child.values[t - 1]

        # Truncate left child
        full_child.keys = full_child.keys[:t - 1]
        full_child.values = full_child.values[:t - 1]
        if not full_child.leaf:
            full_child.children = full_child.children[:t]

        # Insert new child and median into parent
        parent.children.insert(idx + 1, new_child)
        parent.keys.insert(idx, median_key)
        parent.values.insert(idx, median_val)

    def _traverse(self, node: _Node, out: List[Tuple[str, Any]]) -> None:
        for i, key in enumerate(node.keys):
            if not node.leaf:
                self._traverse(node.children[i], out)
            out.append((key, node.values[i]))
        if not node.leaf:
            self._traverse(node.children[-1], out)
