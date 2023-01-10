for i in range(1,5):
    for j in range(1,8):
        if i == 4 or i+j==5 or j-i==3:
            print("*",end="")
        else:
            print(end=" ")
    print()
