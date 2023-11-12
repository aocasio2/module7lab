# alvin ocasio jr
# 11/12/23
# Problem 1

import math

def areaOfCircle(r):
    return math.pi * r**2

radius = 5
print(f"The area of a circle with radius {radius} is {areaOfCircle(radius)}")

# Problem 2
def checkRange(number):
    if number in range(1, 10):
        print(f"{number} is in the range.")
    else:
        print(f"{number} is not in the range.")

num = 7
checkRange(num)
# Problem 3

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [5, 2, 7, -1]
print(f"The result of multiplying all numbers in the list is {multiplyList(numbers)}")

# Problem 4
def uniqueList(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

original_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"The original list with unique elements is {uniqueList(original_list)}")
#problem 5
import turtle

def drawSquare(t, sz):
    """"""Get turtle t to draw a square of sz side""""""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.screen()

alex = turtle.turle()
alex.color("blue")

wn.exitonclick()
# Problem 6
class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.model} {str(self.year)} {self.color} {self.type} {self.manufacturer}"

car1 = Car("Sports", 2012, "Blue", "Convertible", "XYZ Motors")
car2 = Car("Sedan", 2020, "Black", "Sedan", "ABC Cars")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
