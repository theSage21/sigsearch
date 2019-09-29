# SigSearch

Search for algorithms by type signature.


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
