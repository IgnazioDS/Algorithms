import random, string, json
from btree_kv import BTreeKV

def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

def test_insert_and_search():
    tree = BTreeKV()
    tree.set("alpha", 1)
    tree.set("beta", {"x":2})
    tree.set("gamma", [3,4])
    assert tree.search("alpha") == 1
    assert tree.search("beta") == {"x":2}
    assert tree.search("gamma") == [3,4]
    assert tree.search("missing") is None

def test_order_traversal():
    tree = BTreeKV()
    for k in ["d","b","a","c","e"]:
        tree.set(k, k.upper())
    items = tree.items()
    keys = [k for k,_ in items]
    assert keys == sorted(keys)

def test_random_invariants():
    tree = BTreeKV()
    kv = {}
    for _ in range(1000):
        k = random_key()
        v = random.randint(0, 10000)
        kv[k] = v
        tree.set(k, v)
    # verify all present
    for k, v in kv.items():
        assert tree.search(k) == v
