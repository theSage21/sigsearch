# SigSearch

- I was reading a paper recently about [Signature Matching: A Key to Reuse](https://www.cs.cmu.edu/~wing/publications/ZaremskiWing93.pdf)
- What if you could discover algorithms via their type signatures?
- Search for algorithms by type signature.
- For example, what algorithms are capable of taking a matrix and returning a number?
    - `(x: List[List[float]]) -> float`
- Or which algorithms can reduce two numbers to a single one?
    - `(x: int, y: int) -> int`

## Todo

If you have ideas/usecases/code to improve on this, open an issue!

- [x] basic type parsing
- [x] simple search for type sigs
- [ ] use a larger database of algorithms (wiki?)
- [ ] web service


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
0      0    <function insertion_sort at 0x7fec2509f8c8>
1      0    <function selection_sort at 0x7fec2509f7b8>
2      0    <function merge_sort at 0x7fec2509f950>
3      0    <function bubble_sort at 0x7fec2509f840>
4      2.0  <function quick_sort at 0x7fec2509f9d8>
5      3.0  <function linear_search at 0x7fec2509fa60>
6      3.0  <function binary_search at 0x7fec2509fae8>
----------------------------------------------------------------------------------------------------
```

```bash
python -m sigsearch '(x: Sequence[int], y: int) -> int'
----------------------------------------------------------------------------------------------------
Searching for this signature: 
def fn(x: Sequence[int], y: int)->int:
    pass
----------------------------------------------------------------------------------------------------
Index  Dist  Fn
0      0    <function linear_search at 0x7fab42b37a60>
1      0    <function binary_search at 0x7fab42b37ae8>
2      3.0  <function bubble_sort at 0x7fab42b37840>
3      3.0  <function insertion_sort at 0x7fab42b378c8>
4      3.0  <function merge_sort at 0x7fab42b37950>
5      3.0  <function selection_sort at 0x7fab42b377b8>
6      4.0  <function quick_sort at 0x7fab42b379d8>
----------------------------------------------------------------------------------------------------
```
