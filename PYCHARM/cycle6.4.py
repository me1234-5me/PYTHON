import csv
f=open("D:\csv.csv",'r')
content=csv.reader(f)
for x in content:
    print(x)