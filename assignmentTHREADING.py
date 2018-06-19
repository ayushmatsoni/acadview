#QUESTION1
import threading
import time
import math

class Message(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(5)
        print("HELLO")
t=Message()
t.start()
t.join()
#QUESTION2
import threading
import time
import math
class Factorial(threading.Thread):
    def __init__ (self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(2)
        print("FACTORIAL OF GIVEN NO--> %d"%math.factorial(self.h))
fact=1
time.sleep(2)
i=int(input("ENTER ANY NUMBER"))
thread1=Factorial(i)
thread1.start()
thread1.join()

#QUESTION3

class LIST(threading.Thread):
    def __init__ (self,i,timer):
        threading.Thread.__init__(self)
        self.h = i
        self.timer = timer
    def run(self):
            #time.sleep(self.timer)
            print(l[self.h])

j=0
x=0
l=[]
print("ENTER THE LIST VALUES-->")
for j in range (0,5):
   x=int(input())
   l.append(x)

print("")
print("VALUES ARE-->")
j=0
timer=2
while j<=(len(l)-1):
    t=LIST(j,timer)
    time.sleep(timer)
    t.start()
    #j=j+1
    timer=timer+2
    t.join()
    j=j+1

#QUESTION4

class Number(threading.Thread):
    def __init__ (self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(0.5)
        print(self.h)
print("NUMBERS FROM 1 TO 10 ARE->")
for i in range (0,11):
    th=Number(i)
    th.start()
    th.join()

