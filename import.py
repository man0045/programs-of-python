# # import datetime
# # t=datetime.time(9,35,12,123)
# # print(t)

# # print(f"HOUR={t.hour}")
# # print(f"minute={t.minute}")
# # print(f"microsecond={t.microsecond}")
# days= {'mon','tue','wed','thu'}
# enum_days = enumerate(days)
# print(type(enum_days))

# print(list(enum_days))

# enum_days = enumerate(days, 5)
# print(list(enum_days))
# k=['ABES','Engineering','college','Ghaziabad']
# for i in enumerate(k):
#     print(i)

# x=[2,8,1,4,5,3,7]
# print("sorted lis returned : "),
# print(sorted(x))

# print("reverse sort : "),
# print(sorted(x,reverse = True))
# print("Original list not modified : ")
# print(x)
# s='YELLOW'
# print(list(reversed(s)))
# t=('p','Y','T','H','O','N')
# print(list(reversed(t)))
# r=range(5,9)
# print(list(reversed(r)))
# l=[1,2,4,3,5]
# print(list(reversed(l)))
# text="This is a \n normal string"
# print(text)
# raw_text = r"this is a \n raw string"
# print(raw_text)
# import re
# string="ABES Engineering College"
# ma=re.search("AB",string)
# print(ma)
# if(ma):
#     print("Search Successfull")
# else:
#     print("Search unsuccessfull")



# string="String sample Test"
# ma=re.match("Test",string)
# print(ma)
# if(ma):
#     print("Search Successfull")
# else:
#     print("Search unsuccessfull")
# string="Test sample String"
# ma=re.match("Test",string)
# print(ma)
# if(ma):
#     print("Search Successfull")
# else:
#     print("Search unsuccessfull")
# string="Test String sample Test"
# ma=re.findall("Test",string)
# print(ma)
# if(ma):
#     print("Search Successfull")
# else:
#     print("Search unsuccessfull")

# pattern ="i"
# string1 = "Information is immediate"
# s1=re.findall(pattern , string1 , flags=re.IGNORECASE)
# print(s1)
import re
pattern = "@"
string1="a@a.com"
string2="a.com"
s1=re.findall(pattern,string1)
print(s1)
pattern="@\w\."
string1="a@a.com"
s1=re.findall(pattern,string1)
print(s1)