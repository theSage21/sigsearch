# SigSearch

Search for algorithms by type signature.


```bash
python -m sigsearch `(x: Sequence[int]) -> Sequence[int]`
----------------------------------------------------------------------------------------------------
Searching for this signature: 
def fn(x: Sequence[int]) -> Sequence[int]:
    pass
----------------------------------------------------------------------------------------------------
0      Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(0, 1, 2, 3, 2, 3), dist=0.0, is_original=False)
1      Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(0, 1, 2, 3, 2, 3), dist=0.0, is_original=False)
2      Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(0, 1, 2, 3, 2, 3), dist=0, is_original=True)
3      Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(0, 1, 2, 3, 2, 3), dist=0, is_original=True)
4      Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(0, 1, 2, 3), dist=2.0, is_original=False)
5      Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(0, 1, 2, 3), dist=2.0, is_original=False)
6      Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(0, 2, 3), dist=3.0, is_original=False)
7      Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(1, 2, 3), dist=3.0, is_original=False)
8      Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(1, 2, 3), dist=3.0, is_original=False)
9      Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(0, 2, 3), dist=3.0, is_original=False)
10     Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(2, 3), dist=4.0, is_original=False)
11     Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(2, 3), dist=4.0, is_original=False)
12     Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(1,), dist=5.0, is_original=False)
13     Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(0,), dist=5.0, is_original=False)
14     Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(2,), dist=5.0, is_original=False)
15     Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(1,), dist=5.0, is_original=False)
16     Entry(fn=<function bubble_sort at 0x7f8239628840>, prefix=(3,), dist=5.0, is_original=False)
17     Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(2,), dist=5.0, is_original=False)
18     Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(3,), dist=5.0, is_original=False)
19     Entry(fn=<function merge_sort at 0x7f82396288c8>, prefix=(0,), dist=5.0, is_original=False)
----------------------------------------------------------------------------------------------------

```
