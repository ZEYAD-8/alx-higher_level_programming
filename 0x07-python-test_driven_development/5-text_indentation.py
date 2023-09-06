#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """
        Print a text with two new lines after each '.', '?', and ':' character.

        Args:
        text (str): The input text to be formatted and printed.

        Returns:
        None: This function doesn't return a value; it prints the formatted text directly.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    character = 0
    while character < len(text) and text[character] == ' ':
        character += 1

    while character < len(text):
        print(text[character], end="")
        if text[character] == "\n" or text[character] in ".?:":
            if text[character] in "?.:":
                print("\n")
            character += 1
            while character < len(text) and text[character] == ' ':
                character += 1
            continue
        character += 1
