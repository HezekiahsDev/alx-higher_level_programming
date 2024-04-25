#!/usr/bin/python3
"""
This script defines a  python module that finds the
peakn in a list of unsorted integer
"""


def find_peak(list_of_integers):

    """Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list of int): List of integers to find peak of.

    Returns:
        int or None: Peak of list_of_integers or None if list is empty
    """
    size = len(list_of_integers)
    step = size // 2
    mid = size // 2

    if size == 0:
        return None

    while True:
        step = step // 2
        if(mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if step // 2 == 0:
                step = 2
            mid = mid + step // 2
        elif step > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if step // 2 == 0:
                step = 2
            mid = mid - step // 2
        else:
            return list_of_integers[mid]
