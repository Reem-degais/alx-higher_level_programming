#!/usr/bin/python3

def uniq_add(my_list=[]):
    b = set(my_list)
    x = 0
    for i in b:
        x += i
    return (x)
