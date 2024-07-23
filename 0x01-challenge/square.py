#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square with a private attribute instance
attribute `size`. The size attribute is crucial for a square, many things
depend on it (area computation, parameter computation, etc...).
By keeping the size attribute private, the class can ensure control over
its type and value, thus maintaining the integrety of data.

The size attribute must be a non-negative integer.
"""


class Square:
    """
    Square class blueprint.

    Attributes:
        __size (int): The size of the square, must be >= 0.

    """

    def __init__(self, size=0):
        """
        Initialize the Square's instance private attribute `size`

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not positive.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        Sets the size of the square.

        Args:
            new_size (int): The size of the square.

        Raises:
            TypeError: if new_size is not an integer.
            ValueError: if new_size is not positive.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be and integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")

        # if the above if statements are false, size is valid
        self.__size = new_size

    def area(self):
        """ Area of the square """
        return self.size * self.size

    def permiter(self):
        """ Perimeter of the square """
        return self.size * 4

    def __str__(self):
        return "{}".format(self.size)

if __name__ == "__main__":

    s = Square(12)
    print(s)
    print(s.area())
    print(s.permiter())
