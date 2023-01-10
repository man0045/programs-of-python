n = int(input().strip())

ar = list(map(int, input().rstrip().split()))
count=0
for i in range(n-1):
    if(ar[i]==ar[i+1]):
        count+=1 
print(int(count))
        
##### solved by using discussion
ar.sort()
let count = 0
for(let i=0;i<n-1;i++){
    if(ar[i]===ar[i+1]){
            count +=1
            i+=1            
        }
    }
    return count