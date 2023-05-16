#!/usr/bin/python3

def no_c(my_string):
    list_of_str = list(my_string)
    for i in list_of_str:
        if i == "C" or i == "c":
            list_of_str.remove(i)
    return("".join(list_of_str))
