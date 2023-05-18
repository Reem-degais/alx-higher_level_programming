#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for x in a:
        for y in a_dictionary:
            if x == y:
                print("{}: {}".format(y, a_dictionary[y]))
