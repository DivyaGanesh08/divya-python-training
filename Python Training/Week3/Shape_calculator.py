
class Shape():

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

choice = input("Enter Shape (Rectangle / Circle): ")

if choice.lower() == "rectangle":
    length = float(input("Enter Length: "))
    breadth = float(input("Enter Breadth: "))
    shape = Rectangle(length, breadth)
    print("Area of Rectangle:", shape.area())

elif choice.lower() == "circle":
    radius = float(input("Enter Radius: "))
    shape = Circle(radius)
    print("Area of Circle:", shape.area())

else:
    print("Invalid Shape")