#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list and not idx < 0 and len(my_list) > idx:
        return (my_list[idx])
    else:
        return None
