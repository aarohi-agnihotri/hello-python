# area of a circle = pi r*r
# circumference of a circle = 2 pi r

import math

def circle(radius):
    # 3.14 * radius ** 2
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference # returns a tuple (area, circumference)
    # technically, python wraps them in a tuple behind the scenes, so above line is same as:
    # return (area, circumference) # tuple

radius = float(input("Enter radius of a cricle: "))

# and then unpacking on this line :
area_of_circle, circumference_of_circle = circle(radius)

# ---------handling precision-------------- 
# f"{x:.2f}" uses modern string formatting for fixed decimal output, x is variable
print(f"Area of a circle: {area_of_circle: .2f}")
print(f"Circumference of a circle: {circumference_of_circle: .2f}")

# simple printing -
# print("Area of a circle: ", area_of_circle)
# print("Circumference of a circle: ", circumference_of_circle)