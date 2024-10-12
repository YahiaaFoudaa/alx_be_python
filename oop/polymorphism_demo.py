import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return π * self.radius^2