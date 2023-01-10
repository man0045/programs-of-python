def kangaroo(x1, v1, x2, v2):
    jump_count = x2-x1
    for i in range(jump_count):
        x1 = x1+v1
        x2 = x2+v2
        if x1==x2:
            return 'YES'
    return "NO"
            