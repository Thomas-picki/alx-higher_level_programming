#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for idx, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[idx]
            return a_dictionary
