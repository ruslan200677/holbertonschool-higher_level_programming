#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())
    for i, a in sort:
        print("{}: {}".format(i, a))
