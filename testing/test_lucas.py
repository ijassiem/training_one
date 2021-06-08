"""Test module."""

import lucas.lucas as p
import unittest

"""This module contains a class for testing the lucas module."""


class TestPokemon(unittest.TestCase):
    """This class, tests the lucas module.

    This test class contains a set of test methods for testing a class iterator and a
    generator function that both provide the lucas number sequence.
    """

    LUCAS_LIST = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571]

    def test_lucas_class_iterator(self):
        """Test lucas class iterator."""
        my_obj = p.MyLucas(1000)
        cnt = 0
        for val in my_obj:
            print(val, "---", self.LUCAS_LIST[cnt])
            assert val == self.LUCAS_LIST[cnt]
            cnt += 1

    def test_lucas_generator(self):
        """Test lucas generator function."""
        my_lucas = p.lucas(1000)
        cnt = 0
        for value in my_lucas:
            print(value, "---", self.LUCAS_LIST[cnt])
            assert value == self.LUCAS_LIST[cnt]
            cnt += 1
