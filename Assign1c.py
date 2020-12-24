# Python program to find diameter, circumference, and area of a circle from radius given by user

"""
Diameter of a Circle = 2r = 2 * radius
Area of a circle is: A = πr² =  π * radius * radius
Circumference of a Circle = 2πr = 2 * π * radius
D = 2 * r
C = 2 * PI * r
A = PI * r2 
"""


r = int(input("Enter the radius of circle : "))
print(r)
d = 2 * r
c = 2 * 3.14 * r
a = 3.14 * (r * r)
print("\nRadius = ", r, "units")
print("Diameter = ", d, "units")
print("Circumference = ", c, "units")
print("Area = ", a, " sq. units")


""" 
Enter the radius of circle : 10
Radius =  10 units
Diameter =  20 units
Circumference =  62.800000000000004 units
Area =  314.0  sq. units 
"""
