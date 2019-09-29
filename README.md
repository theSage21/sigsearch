# SigSearch

Search for algorithms by type signature.


```bash
python -m sigsearch `(x: Sequence[int]) -> Sequence[int]`
----------------------------------------------------------------------------------------------------
Searching for this signature: 
def fn(x:Sequence[float]) -> Sequence[float]:
    pass
----------------------------------------------------------------------------------------------------
0      Entry(fn=<function bubble_sort at 0x7f2564ac08c8>, prefix=(1,), dist=5.0, is_original=False)
1      Entry(fn=<function merge_sort at 0x7f2564ac0840>, prefix=(0,), dist=5.0, is_original=False)
2      Entry(fn=<function merge_sort at 0x7f2564ac0840>, prefix=(2,), dist=5.0, is_original=False)
3      Entry(fn=<function merge_sort at 0x7f2564ac0840>, prefix=(1,), dist=5.0, is_original=False)
4      Entry(fn=<function bubble_sort at 0x7f2564ac08c8>, prefix=(0,), dist=5.0, is_original=False)
5      Entry(fn=<function bubble_sort at 0x7f2564ac08c8>, prefix=(2,), dist=5.0, is_original=False)
----------------------------------------------------------------------------------------------------
```
