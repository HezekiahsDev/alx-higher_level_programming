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

        @property
        def size(self):
            """This program calculates the size of a square
            Return: size
            """

            return self.__size

        @size.setter
        def size(self, value):
            """set size of square
            Args:
                self: itself
                value: value to set
            Raise:
                TypeError: invalid type
                ValueError: invalid value
            """

            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """Calculate area of a square
                Return: size
                """

            Area = self.__size ** 2

            return Area
