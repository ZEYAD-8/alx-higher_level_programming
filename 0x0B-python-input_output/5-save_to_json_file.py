#!/usr/bin/python3
"""
Contains the "save_to_json_file" function
"""


import json
def save_to_json_file(my_obj, filename):
    """saves the contect of my_obj in a json file"""
    if filename == "":
        return
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)
