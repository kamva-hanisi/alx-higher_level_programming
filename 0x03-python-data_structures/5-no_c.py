#!/usr/bin/python3

def no_c(my_string):

    char = my_string.replace({ord('c'): None})
    char = char.replace({ord('C'): None})
    return char
