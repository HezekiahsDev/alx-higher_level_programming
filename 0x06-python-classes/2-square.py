#!/usr/bin/python3
"""Module define square with ref to some init class"""

class Square:
    """Square in ref to a public class - square"""

    def __init__(self, size=0):
        """set class - square
        Args:
            size: size
        Raise:
            TypeError: size type not valid (not an int)
            ValueError: invalid value (less than zero)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
