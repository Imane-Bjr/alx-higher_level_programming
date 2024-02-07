#!/usr/bin/python3
'''Square module'''


class Square:
    '''A class to create squares'''

    def __init__(self, size=0):
        """[summary]

        Args:
            size (int, optional): [description]. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """[property to get size]

        Returns:
            [int]: [square size]
        """
        return self.__size

    def area(self):
        """[Calculate area]

        Returns:
            [int]: [square area]
        """
        return self.__size*self.__size

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value (int): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print a graphical representation
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
