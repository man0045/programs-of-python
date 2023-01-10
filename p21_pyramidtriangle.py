n=int(input("enter the number of star"))
for j in range(1,n):
    for i in range(1,n):
        if j-i==2 or i-j==3 or j-i==3:
            print("*",end="")
        else:
            print(end=" ")
    print()