for i in range(0,5):
    for j in range(0,5):
        if(j-i==2 or i+j==2 or i-j==2 or i+j==6):
            print("*",end="")
        else:
            print(end=" ")
    print()