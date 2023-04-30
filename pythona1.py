# def greater(a):
#     b=int(input("enter the second number b "))
#     if(a>b):
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# a=int(input("Enter the first number a "))
# # greater(a)
# def greater(x,y):
#     if(x>y):
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# a=int(input("Enter the first number a "))
# b=int(input("enter the second number b"))
# greater(a,b)
# def addition(a,b):
#     sum=a+b
#     return sum
# a,b = map(int,input().split())
# x=addition(a,b)
# print(x)
# def add(a,b,c):
#     return (a+b+c)
# print(add(3,4,5))
# def fruits(*args):
#     for fruit in args:
#         print(fruit)
# fruits("orange ","Banana","Apple","Grapes")
# def fruits(**kwargs):
#     print(kwargs)
#     for fruits in kwargs.values():
#         print()
# # fruits(fruit1="Orange", fruits="Banana", fruits3="Apple", fruit4="Grapes")
# a=3
# print("Gloabal ", a)
# def fun_scope():
#     a=4
#     print("inside fun scope",a )
#     def fun_scope():
#         a=5
#         print("Inside Fun_scope_1", a)
#     fun_scope_1()
# fun_scope()
# import re
# string ="ABES Engineering Collage"
# ma =re.search("AB",string)
# print(ma)
# if(ma):
#     print("Search Successfuly")
# else:
#     print("search is unsuccessfull")
# import re
# string ="Test String sample Test"
# ma =re.findall("Test",string)
# print(ma)
# if(ma):
#     print("Search Successfuly")
# else:
#     print("search is unsuccessfull")
# i = 5
# while True:
#     if(i%0O11==0):
#         break
#         print(i)
#     i=+1
# while True:
#     if i%3 == 0:
#         break     
#         print(i)
#         i + = 1
import re
pattern = "i"
string1="Information is immediate"
s1=re.findall(pattern,string1, flag, CASEIGNORANCE)