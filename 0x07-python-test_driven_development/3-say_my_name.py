#!/usr/bin/python3 
"""Defines a name-printing function.""" 
 
 
def say_my_name(first_name, last_name=""): 
    """ 
    Print a personalized message with the provided first name and last name. 
 
    Args: 
    first_name (str): The first name to include in the message. 
    last_name (str): The last name to include in the message. 
 
    Returns: 
    None: This function doesn't return a value, it prints the message directly. 
    """ 
    if not isinstance(first_name, str): 
        raise TypeError("First Name must be of type string.")

    if not isinstance(last_name, str): 
        raise TypeError("second Name must be of type string.")
    
    print("My name is {} {}".format(first_name, last_name))
