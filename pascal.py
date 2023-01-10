n=int(input("enter n"))
for i in range(1,n):
    for j in range(1,n+3):
        if(i+j>n):
            i=i+1
            print(i,end="")
        else:
            print(end=" ")
        print()