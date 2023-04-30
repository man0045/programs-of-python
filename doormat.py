# cook your dish here
def countOccurrances(n, d):
    count = 0
 
    # Loop to find the digits of N
    while (n > 0):
 
        # check if the digit is D
        if(n % 10 == d):
            count = count + 1
  
        n = n // 10
 
    return count
 
# Driver code
d = 7
n = int(input(""))

print(countOccurrances(n, d))