#!/usr/bin/python3

def no_c(my_string):

    char = my_string.translate({ord('c'): None})
    char = char.translate({ord('C'): None})
    return char
