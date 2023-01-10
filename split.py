# x=str(input("enter the charecter"))
# x=x.split()
# print(x)
# x="_".join(x)
# print(x)
def split_and_join(line):
    
        # line = str(input("enter "));
        line=line.split()
        # "_".join(line)
        line="-".join(line)
        # # print(line)
        return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)