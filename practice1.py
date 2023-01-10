#x=int(input("enter the number"))
for i  in range(10001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
       # result == num
        digit = i%10
        result= result + digit**n 
        i=i//10
       # result==num
    if(num==result):
        print(result)

