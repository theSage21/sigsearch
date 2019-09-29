import argparse
import typing
from .core import Index
from .algos import all_fns

parser = argparse.ArgumentParser(prog="python -m typesearch")
parser.add_argument(
    "query",
    help="""
    Type in the function signature to search for.
    For example,
            (x: Sequence[float]) -> float
            (x: int, y: int) -> int
            (x: List[List[int]] -> int
    """,
)
args = parser.parse_args()
# build index
index = Index()
for fn in all_fns:
    index.add(fn)
# build query fn
q = f"""def fn{args.query}:
    pass"""
print(("-" * 100)[:100])
print("Searching for this signature: ")
print(q)
print(("-" * 100)[:100])
ctx = {k: getattr(typing, k) for k in typing.__all__}
exec(q, ctx)
# search
results = list(index.find(ctx["fn"]))
for index, candidate in enumerate(results):
    print(f"{index:<5} ", candidate)
print(("-" * 100)[:100])
