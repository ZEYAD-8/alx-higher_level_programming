#!/usr/bin/python3
def search_replace(my_list, search, replace):
    searchList = []
    for i in my_list:
        if search == i:
            searchList.append(replace)
        else:
            searchList.append(i)
    return searchList
