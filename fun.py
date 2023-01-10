n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
count=0
for i in range(n-m+1):
    if(sum(s[i:i+1])==d):
        count+=1
print(count)