def diagonalDifference(arr):
    # Write your code here
    x=0
    y=0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                x=x+arr[i][j]
            elif(i+j==n+1):
                y=y+arr[i][j]
            else:
                continue
    return x-y
            
            
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
