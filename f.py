n=int(input(""))
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
    n=min(l)
    a=n-x
if(a==0):
    print(x)
else:
    print(a)
