import datetime
from datetime import date
import time
import os
import math



#question1
#In python, the time is stored in tuple, so that it's easy for us to understand, These python tuples are made of nine numbers.
#Index	                               Field	                             Domain of Values
#0	                                   Year                                  (4 digits)	Ex.- 1995
#1	                                   Month	                              1 to 12
#2	                                   Day	                                  1 to 31
#3	                                   Hour                                  0 to 23
#4	                                   Minute	                              0 to 59
#5	                                   Second	                              0 to 61 (60/61 are leap seconds)
#6	                                   Day of Week	                          0 to 6 (Monday to Sunday)
#7	                                   Day of Year	                          1 to 366 (Julian day)
#8	                                   DST	                                  -1,0,1



#question2
print("QUESTION2")
print("DATE AND TIME")
print(time.asctime(time.localtime()))
print("")

#question3
print("QUESTION3")
a='2010-01-31'
dat1=datetime.datetime.strptime(a,"%Y-%m-%d")
print("2010-01-31---> month-->")
print(dat1.month)
print("TODAY'S DATE-->")
print(date.today())
dt=str(date.today())
dat2=datetime.datetime.strptime(dt,"%Y-%m-%d")
print("Today's month")
print(dat2.month)
print("")


#question4
print("Today's time")
print(time.asctime(time.localtime()))
tod=str(time.asctime(time.localtime()))
print("Extracted day")
tod.split(" ",1)
for i in range(0,3):
    if i!=' ':
        print(tod[i],end="")
print("")
print("")

#question5
print("QUESTION5")
print("Today's Date")
print(date.today())
td=str(date.today())
d=str(td[8])+str(td[9])
print("Extracted Date->")
print(d)
print("")
#question6
print("QUESTION6")
print(time.asctime(time.localtime()))
print("")

#quetion7

print("QUESTION7")
num=int(input("ENTER THE NUMBER-->"))
print(math.factorial(num))
print("")

#question8

print("QUESTION8")
n1=int(input("ENTER THE NUMBER 1-->"))
n2=int(input("ENTER THE NUMBER 2-->"))
print(math.gcd(n1,n2))
print("")

#question9

print("QUESTION9")
print(os.getcwd())
print(os.environ)