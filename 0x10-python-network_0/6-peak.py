#!/usr/bin/python3
""" finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    max_int = None
    if list_of_integers is None:
        return None
    else:
        for i in list_of_integers:
            if max_int is None or max_int < i:
                max_int = i
        return max_int
