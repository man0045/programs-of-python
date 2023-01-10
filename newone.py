n=int(input("enter the number of star"))
for col in range(n):
    for row in range(n):
        if col==(n-1) or row==0 or row==col :
            print("*",end="")
        else:
            print(end=" ")
    print()