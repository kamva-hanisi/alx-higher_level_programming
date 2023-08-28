#!/usr/bin/python3
def safe_print_integer(value):

    "
     my_list: The list containing elements
      x: The number of elements to print

    Return:
      The real number of integers printed
    "
    try:
        print("{:d}".format(value), end="\n")
        return (True)
    except (ValueError, TypeError):
        return (False)
