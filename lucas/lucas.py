"""This module contains an iterator class and a generator function for providing the lucas number sequence."""


import time


class MyLucas:
    """This class creates an iterator which returns the lucas sequence of numbers."""

    def __init__(self, max_no):
        """Initialise MyLucas class with a maximum sequence value."""
        self.max_no = max_no

    def __iter__(self):
        """Inititialise first two lucas numbers and return iterator object.

        Returns
        ------
        MyLucas object
            MyLucas class object as an iterator..
        """
        self.a = 2
        self.b = 1
        return self

    def __next__(self):
        """Provide next number in lucas sequence.

        This method computes and returns the next number in the lucas numbers sequence, until the maximum number (max_no) is reached.
        Example of the Lucas numbers up to 123 : 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123

        Returns
        ------
        int
            Next lucas number in sequence.

        Raises
        ------
        StopIteration
            Raises a StopIteration when iteration reaches a maximum number of times (max_no).
        """
        if self.a < self.max_no:
            x = self.a
            y = self.b
            self.a = y
            self.b = x + y
            return x
        else:
            raise StopIteration


def lucas(max_val):
    """Provide the Lucas number sequence.

    This generator function provides the sequence of lucas numbers up to the value specified by max_val.
    Example of the Lucas numbers up to 123 : 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123

    Parameters
    ----------
    max_val : int
        This value specifies the maximium number or range of the lucas sequence.

    Yields
    ------
    int
        Lucas sequence of numbers
    """
    a = 2
    b = 1
    while a < max_val:
        time.sleep(0.2)
        x = a
        y = b
        a = y
        b = x + y
        yield x


if __name__ == "__main__":
    for v in MyLucas(1000):
        print(v)
    for w in lucas(124):
        print(w)
