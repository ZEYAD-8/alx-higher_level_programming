#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(-1, len(my_list) * -1, -1):
        print("{:d}".format(my_list[i]))
    # There's a variety of ways here, you can use list.reverse method
    # or you can reverse the list in a new list using my_list[::-1]
    # All roads lead to Rome
