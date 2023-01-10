count=0
d={'U' : 1 , 'D' : -1}
for i in path:
    count += d[i]
    if(count == 0 and i== 'U'):
        count +=1
return count