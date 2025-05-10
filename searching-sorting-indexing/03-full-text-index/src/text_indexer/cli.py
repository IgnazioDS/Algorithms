import argparse, pathlib, time
from . import SuffixArray

def main():
    p=argparse.ArgumentParser()
    p.add_argument("file",type=pathlib.Path)
    p.add_argument("pattern")
    args=p.parse_args()
    text=args.file.read_text(encoding='utf-8',errors='ignore')
    t=time.time()
    sa=SuffixArray(text)
    print(f"Index built in {time.time()-t:.3f}s")
    t=time.time()
    hits=sa.find(args.pattern)
    print(f"Search in {time.time()-t:.3f}s found {len(hits)} hits: {hits}")
if __name__=='__main__':
    main()
