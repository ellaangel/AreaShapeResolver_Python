class Shape:

    def __init__(self, a, b):
      self.a = a
      self.b = b
      

    def get_area(self):
        return self.a * self.b
    
    def __str__(self):
        return f"The sum of area is: {self.get_area()}"

    def __repr__(self):
        return f"The Class name: {self.__class__}, The sum of area is: {self.get_area()}"

class Rectangle(Shape):
  pass

class Square(Shape):

    def __init__(self, a, b):
      super().__init__(a, b)


class Triangle(Shape):
    def get_area(self):
        return super().get_area() / 2

class Circle(Shape):
    def __init__(self, a):
      self.a = a

    def get_area(self, *arg):
        return self.a **2 * 3.14

from math import sqrt

class Hexago(Shape):
    def __init__(self, a):
      self.a = a
    
    def get_area(self):
        return (3* sqrt(3) * self.a **2) /2


## To check:

test1 = Shape(5, 2)
test2 = Rectangle(5, 10)
test3 = Square(5, 3)
test4 = Triangle(5, 9)
test5 = Circle(5)
test6 = Hexago(5)

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)

print(Shape.get_area)
