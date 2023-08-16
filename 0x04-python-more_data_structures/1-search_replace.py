#!/usr/bin/python3
def search_replace(my_list, search, replace):

      new_check = [replace if j == search else j for j in my_list]

    return new_check
