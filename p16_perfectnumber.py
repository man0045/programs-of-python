n=int(input("enter the number"))
x=0
for i in range(1,n):
    s=n%i
    if(s==0):
        x=x+i
if(x==n):
    print("number is perfect")
else:
    print("number is not perfect")
