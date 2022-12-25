y=int(input("Enter number :"))
if((y%400==0) or (y%100!=0) and (y%4==0)):
    print("Leap Year")
else:
    print("Not a Leap year")