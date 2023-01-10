for j in range(1,5):
    for i in range(1,5):
        if i == j or i+1 == j or i+2==j or i+3==j:
             print("*",end="")
        else:
            print(end=" ")
    print()

