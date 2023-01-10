
s=int(input())
#print(s.isalnum())
for i in range(0,s):
    i=i+1
    if(65<=i<=90):
        print("uppercase")
    elif(97<=i<=122):
        print("lowercase")
    else:
        print("alphanmeric")