import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#
def icecreamParlor(m, arr):
    # c=int(input("cost"))
    # Write your code here
    for i in range (len(arr)):
        for j in (i+1,len(arr)):
            if(arr[i] + arr[j]==m):
                 return[i+1 , j+1]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         m = int(input().strip())

#         n = int(input().strip())

#         arr = list(map(int, input().rstrip().split()))

#         result = icecreamParlor(m, arr)

#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')

#     fptr.close()