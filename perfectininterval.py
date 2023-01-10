n=int(input("enter the number"))
for i in range(1,n):
    x=0
    for j in range(1,i):
        if(i%j==0):
            x=x+j
    if i==x:
        print(i)