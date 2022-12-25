#Circulate two list of values using in-Built function
print("To circulate two values in a list")
n=int(input("Enter the number of values in the list :"))
l=[]
for i in range(0,n):
    x=int(input("Enter the value :"))
    l.append(x)
a=int(input("Enter number of rotation :"))
for i in range(0,a):
    b=l.pop(0)
    l.append(b)
    print("The circulate list is :",l)
