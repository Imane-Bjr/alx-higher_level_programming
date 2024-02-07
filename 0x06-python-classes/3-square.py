#!/usr/bin/python3
'''Square module'''


class Square:
    '''A class to create squares'''

    def __init__(self, size=0):
        """[summary]

        Args:
            size (int, optional): [description]. Defaults to 0.

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """[Calculate area]

        Returns:
            [int]: [square area]
        """
        return self.__size*self.__size
