#!/usr/bin/python3
"""
script to save and load
"""
import sys
import json


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit()
    save_to_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_file(items, "add_item.json")
