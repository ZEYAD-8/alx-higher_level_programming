#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for item in range(x):
        try:
            print("{}".format(my_list[item]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)
