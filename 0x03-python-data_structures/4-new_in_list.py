#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if my_list and not idx < 0 and len(my_list) > idx:
        new[idx] = element
    return new
