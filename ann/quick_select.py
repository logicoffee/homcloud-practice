from numpy import array, array_split, apply_along_axis, sort
from math import ceil


def quick_select(arr, index):
    p = pivot(arr)
    left = arr[arr < p]
    middle = arr[arr == p]
    left_length = len(left)
    middle_length = len(middle)
    if left_length < index & index <= left_length + middle_length:
        return p

    if left_length >= index:
        return quick_select(left, index)

    right = arr[arr > p]
    return quick_select(right, index - left_length - middle_length)


def pivot(arr):
    length = len(arr) // 5
    if length == 0:
        return sort(arr)[len(arr) // 2]
    sub_arrays = array(array_split(arr[:length * 5], length))
    medians = apply_along_axis(lambda arr5: sort(arr5)[2], 1, sub_arrays)
    return quick_select(medians, ceil(length / 2))
