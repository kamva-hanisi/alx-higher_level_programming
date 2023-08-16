#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    list_dictionary = {}
    for key, value in a_dictionary.items():
        list_dictionary[key] = value * 2
    return list_dictionary
