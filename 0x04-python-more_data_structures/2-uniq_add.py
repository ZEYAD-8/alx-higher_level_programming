#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqItem = set()
    sum_item = 0
    for i in my_list:
        if i not in uniqItem:
            uniqItem.add(i)
            sum_item += int(i)
    return sum_item
