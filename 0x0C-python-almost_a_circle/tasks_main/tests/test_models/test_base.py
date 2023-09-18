#!/usr/bin/python3
"""
Defines unittests for base.py.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_init_(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_number_arg(self):
        """Test 'id' attribute incrementation in the 'Base' class."""
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_None_id(self):
        """
        Tests that an id is not assigned to a 
        new instance if one isn't provided as input.
        """
        base_1 = Base(None)
        base_2 = Base(None)
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_give_id(self):
        """
        Tests that an id can be given when instantiating 
        a new object from the Base Class.
        """
        base_r = Rectangle(10, 5, 6, 6, 90)
        base_s = Square(3, 5, 10, 200)
        base_t = Base(20)
        self.assertEqual(base_r.id, 90)
        self.assertEqual(base_s.id, 200)
        self.assertEqual(base_t.id, 20)

    def test_direct_id(self):
        """Tests that direct assignment of ids works correctly."""
        base_i = Base()
        base_i.id = 18
        self.assertEqual(base_i.id, 18)

    def test_string_id(self):
        """Tests that assigning string values """
        base = Square(8, 10, 4, "Test")
        self.assertEqual(base.id, "Test")

    def test_for_key(self):
        """Tests that assigning Keys and Values """
        base = Base()
        dict = {"key": "Value"}
        base.id = dict
        self.assertEqual(base.id, dict)
        
    def test_for_boll_T(self):
        """Tests that assigning boollen value"""
        Base = Square(2, 4, 5, True)
        self.assertEqual(Base.id, 1)


if __name__ == '__main__':
    unittest.TestCase()
