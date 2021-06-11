"""Test module."""

import cash_register.cash_register as cr
import unittest

"""
This module contains a class for testing the cash_register module.

There are several test methods for testing the cash_register module.
"""


class Test1(unittest.TestCase):
    """Test class."""

    def test_total_integers(self):
        """Test total function with list of integers as input."""
        int_list = [5, 10, 50, 35]
        assert cr.total(int_list) == 100

    def test_total_floats(self):
        """Test total function with floats of integers as input."""
        float_list = [5.1, 10.321, 50.0, 3.98, 4.4]
        self.assertAlmostEqual(cr.total(float_list), 73.801, places=2)

    def test_vat_integer(self):
        """Test vat calculation with integer as input."""
        value = 58
        self.assertAlmostEqual(cr.vat(value), value * 0.15, places=2)

    def test_vat_float(self):
        """Test vat calculation with float as input."""
        value = 412.32
        self.assertAlmostEqual(cr.vat(value), value * 0.15, places=2)

    def test_add_integer(self):
        """Test add function with integers as input."""
        assert cr.add(3, 2) == 3 + 2

    def test_add_float(self):
        """Test add function with floats as input."""
        self.assertAlmostEqual(cr.add(2.21, 4.7), 2.21 + 4.7, places=2)

    def test_print_statement(self):
        """Test print statement."""
        pass
