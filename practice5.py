n=int(input("enter the number of star"))
for j in range(n):
    for i in range(n):
        if i==0 or j==(n-1) or i==j :
            print("*",end="")
        else:
            print(end=" ")
    print()