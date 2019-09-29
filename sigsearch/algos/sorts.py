from typing import Sequence, Union


def bubble_sort(collection: Sequence[Union[float, int]]) -> Sequence[Union[float, int]]:
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def merge_sort(collection: Sequence[Union[float, int]]) -> Sequence[Union[float, int]]:
    def merge(left, right):
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


fns = [bubble_sort, merge_sort]
