#DISTANCE BETWEEN 2 POINTS
import math
print("To find the distance between two points")
x1=int(input("Enter x1 value : "))
y1=int(input("Enter x2 value : "))
x2=int(input("Enter y1 value : "))
y2=int(input("Enter y2 value : "))
d=pow(pow(x2-x1,2)+pow(y2-y1,2),1/2)
print("The distance between the points is",float(d))
