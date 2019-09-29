from typing import Sequence


def selection_sort(arr: Sequence[int]) -> Sequence[int]:
    """
    name: Selection Sort
    link: 'https://en.wikipedia.org/wiki/Selection_sort'
    bst: Ω(n^2)
    avg: Ω(n^2)
    wst: Ω(n^2)
    """


def bubble_sort(arr: Sequence[int]) -> Sequence[int]:
    """
    name: Bubble Sort
    link: 'https://en.wikipedia.org/wiki/Bubble_sort'
    bst: Ω(n)
    avg: Θ(n^2)
    wst: O(n^2)
    """


def insertion_sort(arr: Sequence[int]) -> Sequence[int]:
    """
    name: Insertion Sort
    link: 'https://en.wikipedia.org/wiki/Insertion_sort'
    bst: Ω(n)
    avg: Θ(n^2)
    wst: O(n^2)
    """


def merge_sort(arr: Sequence[int]) -> Sequence[int]:
    """
    name: Merge Sort
    link: 'https://en.wikipedia.org/wiki/Merge_sort'
    bst: Ω(n log(n))
    avg: Θ(n log(n))
    wst: O(n log(n))
    """


def quick_sort(arr: Sequence[int], lo: int = 0, hi: int = None) -> Sequence[int]:
    """
    name: Quick Sort
    link: 'https://en.wikipedia.org/wiki/Quicksort'
    bst: Ω(n log(n))
    avg: Θ(n log(n))
    wst: O(n^2))
    """


fns = [bubble_sort, merge_sort, selection_sort, insertion_sort, quick_sort]
