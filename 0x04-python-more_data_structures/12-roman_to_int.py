#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    decs_check = [roman_dictionary[x] for x in roman_string]
    roman_output = 0
    for i in range(len(decs_check)):
        roman_output += decs_check[i]
        if decs_check[i - 1] < decs_check[i] and i != 0:
            roman_output -= (decs_check[i - 1] + decs_check[i - 1])
    return roman_output
