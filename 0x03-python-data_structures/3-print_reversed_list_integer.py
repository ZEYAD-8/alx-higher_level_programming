#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        new_list = my_list[::-1]
        for i in new_list:
            print("{:d}".format(i))
    # There's a variety of other ways here, you can use list.reverse method
    # or you can iterate over the list from the end
    # All roads lead to Rome
