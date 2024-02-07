#!/usr/bin/python3
'''Square module'''


class Square:
    '''A class to create squares'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        if self.size == 0:
            return ""
        pt = "\n" * self.position[1]
        for i in range(self.size):
            pt = pt + "{}{}".format(" " * self.position[0], "#" * self.size)
            if i < self.size - 1:
                pt = pt + "\n"
        return pt

    @property
    def size(self):
        """[property to get size]

        Returns:
            [int]: [square size]
        """
        return self.__size

    @property
    def position(self):
        return self.__position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self, pend=True):
        """print a graphical representation
        """
        if self.__size is 0 and pend is True:
            print()
        elif self.__size is 0 and pend is False:
            pass
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__size + self.__position[0]):
                    if j >= self.__position[0]:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print()
        return

    @position.setter
    def position(self, value):
        success = True
        success = success and type(value) is tuple and len(value) is 2
        success = success and type(value[0]) is int and type(value[1]) is int
        success = success and value[0] >= 0 and value[1] >= 0
        if success is True:
            self.__position = value
        else:
            raise ValueError("position must be a tuple of 2 positive integers")
