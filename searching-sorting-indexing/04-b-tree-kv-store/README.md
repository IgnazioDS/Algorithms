# 04‑b‑tree‑kv‑store

A minimal **in‑memory B‑tree** (order *t = 3*) exposed as a key‑value store.

* Fixed fan‑out B‑tree with split/insert/search
* Keys are strings, values are arbitrary JSON‑serialisable objects
* Simple CLI:
  ```bash
  python -m btree_kv.cli set foo 123
  python -m btree_kv.cli get foo
  ```
* Unit tests verify:
    * Sorted in‑order traversal
    * Search returns correct values
    * Inserting 1 000 random keys keeps B‑tree invariants

## Structure
```
src/btree_kv/
    __init__.py
    btree.py     # core implementation
    cli.py       # basic REPL / shell commands
tests/
    test_btree.py
```

## Install & run

```bash
pip install -r requirements.txt
pytest    # all green
python -m btree_kv.cli   # interactive shell
```
