import datetime
year = int(input("enter the year").strip())
for year in range(1700,2700):
    if(year%4==0 and year%400==0 and year%100!=0):
        print(datetime(256,5,year))