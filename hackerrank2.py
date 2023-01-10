def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        
        # for j in range(1,i+1):
        print(" "*(n-i) +"#"*i)
        # print("")
    # i=1
    # while(i<=n):
    #     print(" " * (n - i) +"#" * i)
    #     i+=1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
