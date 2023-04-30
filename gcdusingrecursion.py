def gcd(x ,y):
    if(y== 0):
        return x
    else:
        
       return gcd(y , x%y)
    
x = int(input("Enter the first number"))
y = int (input("Enter the second number"))
GCD = gcd(x,y)
print("Gcd of two number x and y is : ")
print(GCD)

