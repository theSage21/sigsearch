# SigSearch

- What if you could discover algorithms via their type signatures?
- Search for algorithms by type signature.
- For example, what algorithms are capable of taking a matrix and returning a number?
    - `(x: List[List[float]]) -> float`
- Or which algorithms can reduce two numbers to a single one?
    - `(x: int, y: int) -> int`


## Usage


- type in a minimal signature in the CLI

```bash
python -m sigsearch '(x: Sequence[int]) -> Sequence[int]'
----------------------------------------------------------------------------------------------------
Searching for this signature: 
def fn(x: Sequence[int]) -> Sequence[int]:
    pass
----------------------------------------------------------------------------------------------------
Index  Dist  Fn
0      0    <function bubble_sort at 0x7f8bc0e1e7b8>
1      0    <function merge_sort at 0x7f8bc0e1e840>
----------------------------------------------------------------------------------------------------
```

## Todo

If you have ideas/usecases/code to improve on this, open an issue!

- [x] basic type parsing
- [x] simple search for type sigs
- [ ] use a larger database of algorithms (wiki?)
- [ ] web service

