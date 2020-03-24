# Python First Task: Create Basic Calculator for Area of a Circle

import math


def areaOfCircle(radius):
    area = math.pi * radius ** 2
    radius = float(radius)
    print(f'The area of a circle with radius {radius} is {area}')


areaOfCircle(40)

# or like this

radius = float(input(f'Enter the radius of a circle '))
area = math.pi * radius ** 2
print(f'The area of a circle with radius {radius} is {area}')
