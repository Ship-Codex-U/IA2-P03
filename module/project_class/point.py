class Point:
    def __init__(self, x_coordinate = -1, y_coordinate = -1, value = -1 , color = "black" ) -> None:
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__value = value
        self.__color = color

    @property
    def x_coordinate(self):
        return self.__x_coordinate
    
    @x_coordinate.setter
    def x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate
        
    @property
    def y_coordinate(self):
        return self.__y_coordinate
    
    @y_coordinate.setter
    def y_coordinate(self, y_coordinate):
        self.__y_coordinate = y_coordinate

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def red(self, color):
        self.__color = color

    def __str__(self):
        return f"({self.__x_coordinate}, {self.__y_coordinate}, {self.__value}, {self.__color})"
        