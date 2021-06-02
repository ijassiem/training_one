"""
This is the cash register module.

This module contains functions to be used by a cash a register.
"""


def total(list):
    """Calculate total."""
    total = 0
    for ele in range(0, len(list)):
        total = total + list[ele]
    return round(total, 2)


def vat(value):
    """Calculate VAT."""
    return round(value * 0.14, 2)


def add(x, y):
    """Add two numbers."""
    return round(x + y, 2)


def print_statement(list):
    """Print a statement."""
    print("\nSTATEMENT")
    print("-----")
    for ele in range(0, len(list)):
        print(list[ele])
    t = total(list)
    v = vat(t)
    grand_total = add(t, v)
    print("-----")
    print(t, "(TOTAL)")
    print(v, "(VAT)")
    print("-----")
    print(grand_total, "(GRAND TOTAL)\n")
