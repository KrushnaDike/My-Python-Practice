from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = 6
        self.breadth = 7

    # def printarea(self):
    #     return self.length * self.breadth

rec1 = Rectangle()
# print(rec1.printarea())