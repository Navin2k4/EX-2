n=int(input("Enter number :"))
p=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            p=True
if p:
    print("Not Prime")
else:
    print("Prime")
