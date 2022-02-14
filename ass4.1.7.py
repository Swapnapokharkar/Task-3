#Calculate surface area and volume of cylinder in python
PI = 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))

sa = 2 * PI * radius * (radius + height)
Volume = PI * radius * radius * height
print("\n The Surface area of a Cylinder = %.2f" %sa)
print(" The Volume of a Cylinder = %.2f" %Volume)