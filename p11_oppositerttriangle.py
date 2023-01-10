n=int(input("enter the number"))
for j in range(n,0,-1):
    for i in range(1,j+1):
        i=i+1
        print(j,end="")
    print()