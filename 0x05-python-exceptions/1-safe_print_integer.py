#!/usr/bin/python3
def safe_print_integer(value):
    """
     value: The value to be printed
    Return:
      True if integer otherwise False

    """
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return (False)
    else:
        return (True)
