#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    char_A = len(tuple_a)
    char_B = len(tuple_b)
# for tuple_a
    if char_A < 1:
        tuple_a = (0, 0)
    elif char_A < 2:
        tuple_a = (tuple_a[0], 0)

# for tuple_b
    if char_B < 1:
        tuple_b = (0, 0)
    elif char_B < 2:
        tuple_b = (tuple_b[0], 0)

    check = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return check
