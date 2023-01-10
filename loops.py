condition1=1
while condition1<=3:
    print(condition1,"outer loop executed")
    condition2=1
    while condition2<=3:
        print(condition2,"inner loop")
        condition2+=1
    condition1+=1
