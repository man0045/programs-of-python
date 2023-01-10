from time import time
s=input()

    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time
    # if(count<k):
    #     print("YES")
    #     continue
    # else:
    #     print("NO")
# for i in range(m):
#     if(a[i]>=0):
#        print("NO")