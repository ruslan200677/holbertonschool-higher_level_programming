#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for int in set(my_list):
        result += int
    return (result)
