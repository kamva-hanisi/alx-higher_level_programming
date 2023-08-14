#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    new_leng = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_leng[i] = 1
        else:
            new_leng[i] = 0
    return new_leng
