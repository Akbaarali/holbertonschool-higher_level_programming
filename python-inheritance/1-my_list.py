#!/usr/bin/python3
"""This module defines a class that inherits from list and prints it sorted.
"""


class MyList(list):
    """Custom list class with a method to print the list sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
