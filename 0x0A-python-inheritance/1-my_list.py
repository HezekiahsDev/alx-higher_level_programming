#!/usr/bin/python3

"""This script defines a custom class that inherits from the list class."""


class MyList(list):
    """A specialized class that extends the functionality of the list class."""

    def print_sorted(self):

        """Prints the elements of the list in a sorted order."""

        print(sorted(self))
