# (Circle Area, Diameter and Circumference) For a circle of radius 2. display the diameter, circumference and area. Use the value 3.14159 for pi. Use the following formulas (r is the radius): diameter = 2*r, circumference = 2*pi*r and area = pi*r^2. [In a later chapter,  we'll introduce Python's math module which contains a higher-precision representation of pi.]

pi = 3.14159
radius = 2

diameter = 2 * radius
print('Diameter =', diameter)
circumference = 2 * pi * radius
print('Circumference =', circumference)
area = pi * radius ** 2
print('Area =', area)