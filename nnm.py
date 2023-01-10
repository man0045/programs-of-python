e=[]
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
k = list(map(int, input().rstrip().split()))
d = list(map(int, input().rstrip().split()))
if(k[0] + d[0]) > b :
    print(-1)
for i in k:
    for j in d:
        x =i+j
        if (x <=b):
            e.append(x)
print(max(e))
