from module.project_class.point import Point

class Points:
    def __init__(self):
        self.__points = []

    def insert_point(self, point : Point):
        self.__points.append(point)

    def insert_point(self, x_coordinate = -1, y_coordinate = -1, value = -1 , color = "black" ):
        self.__points.append(Point(x_coordinate, y_coordinate, value, color))
    
    def get_points(self):
        return self.__points

    def get_inputs(self):
        inputs = []
        for point in self.__points:
            inputs.append((point.x_coordinate, point.y_coordinate))
        return inputs
    
    def get_results(self):
        results = []
        for point in self.__points:
            results.append(point.value)
        return results
    
    def clear(self):
        self.__points.clear()
    
