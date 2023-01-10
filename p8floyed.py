n=int(input("enter the number of rows"))
s=1
for i in range(0,n+1):
    for j in range(1,i+1):
        print(s,end="")
        s=s+1
    print()