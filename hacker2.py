count=0
brr=[16 ,32, 96]
for i in range(1,brr[0]-1):
    i=i+1
    if(brr[0]%i==0):
        count+=1
print(count)

