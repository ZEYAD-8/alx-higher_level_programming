#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i not in "Cc":
            new_string += i
    return new_string
###
# my first solve was like this:
    # new_string = my_string[0:]
    # chars_emitted = i = 0
    # for char in my_string:
    #     i += 1
    #     if char in "Cc":
    #         new_string = new_string[0:i - chars_emitted - 1] + new_string[i - chars_emitted:len(new_string)]
    #         chars_emitted += 1
    # return new_string
# I know i know, still thinking the C way not the python way.
###