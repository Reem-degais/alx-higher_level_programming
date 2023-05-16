#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence == None:
        first = None
    else:
        first = sentence[0]
    return (length, first)
