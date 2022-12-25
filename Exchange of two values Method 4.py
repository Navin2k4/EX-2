#Swappign Using XOR (^) Operator
print("Swapping of two values")
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("The values before swapping :",a," ",b)
a=a^b
b=a^b
a=a^b
print("The values after swapping :",a," ",b)
