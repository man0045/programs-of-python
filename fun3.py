first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
a=0
# k=[23,54,65,21,6,7]

for i in range(len(bill)):
    a=a+bill[i]
    z=(a-bill[n-1])/2 
    k=b-z
print(k) 
    # continue
for i in range(len (bill)):
    a=a+bill[i]
    z=a/2
print("Bon Appetit")