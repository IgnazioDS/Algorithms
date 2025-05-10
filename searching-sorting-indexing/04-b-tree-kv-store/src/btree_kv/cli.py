"""Minimal CLI for the B‑tree key‑value store."""
import argparse, json, sys
from .btree import BTreeKV

store = BTreeKV()

def main():
    parser = argparse.ArgumentParser(prog="btree-kv")
    sub = parser.add_subparsers(dest="cmd", required=True)

    s_set = sub.add_parser("set", help="store a key/value")
    s_set.add_argument("key")
    s_set.add_argument("value")

    s_get = sub.add_parser("get", help="retrieve a value")
    s_get.add_argument("key")

    args = parser.parse_args()

    if args.cmd == "set":
        try:
            value = json.loads(args.value)
        except json.JSONDecodeError:
            value = args.value
        store.set(args.key, value)
    elif args.cmd == "get":
        val = store.search(args.key)
        if val is None:
            print("Key not found", file=sys.stderr)
            sys.exit(1)
        print(json.dumps(val))
if __name__ == "__main__":
    main()
