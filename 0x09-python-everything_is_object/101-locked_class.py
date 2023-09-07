#!/usr/bin/python3
"""
Locked Class Module

This module defines a Python class called LockedClass
that demonstrates the use of __slots__
to restrict the attributes that instances of the class can have.

Usage:
    from locked_class import LockedClass

    # Create an instance of LockedClass
    obj = LockedClass()

    # Assign a value to the 'first_name' attribute
    obj.first_name = "John"

    # Attempt to assign a value to a non-existent attribute
        (will raise an AttributeError)
    obj.last_name = "Doe"
"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
