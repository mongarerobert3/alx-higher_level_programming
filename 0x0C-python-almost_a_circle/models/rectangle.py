#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("heigth"))
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """gets the x value """
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """
            Displays # under the area covered by the rectangle
        """
        if self.__y > 0:
            print('/n' * self.__y, end='')
        
        for i in range(self.height):
            if self.__x > 0:
                print('' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """String representation of the rectangle class"""
        str_rep = "[Rectangle] ({}) {}/{} - {} {}".format(self.id, self.x, self.y, self.__width, self.__height)
        return str_rep

    def update(self, *args, **kwargs):
        """updating display to print to stdout"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ["id", "width", "height", "x", "y"]

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)
        
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y}
            