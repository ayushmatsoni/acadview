import numpy as np
import math

#Q1
print("QUESTION 1")
a=np.random.random((10,1))
print (a)
m=a.mean()
print("THE MEAN OF ELEMENTS-> "+str(m))
print("\n")

#Q2
print("QUESTION 2")
b=np.random.random((20,1))
print(b)
v=b.var()
print("VARIANCE OF ELEMENTS-> "+str(v))
s=b.std()
print("STANDARD DEVIATION-> "+str(s))
print("\n")

#Q3
print("QUESTION 3")
a=np.random.random((10,20))
b=np.random.random((20,25))
#a.dtype=np.float64
#b.dtype=np.float64
#print(a*b)
c=np.matmul(a,b)
print(c)
d=np.sum(c)
print(c.shape)
print("SUM OF ALL ELEMENTS-> "+str(d))
print("\n")

#Q4
print("QUESTION 4")
print("RANDOM ARRAY->")
x=np.random.random((10,1))
print(x)
i=0
l=[]
for i in range(0,10):
    ans=1/(1+math.exp(-(x[i,0])))
    l.append(ans)
print("f(x) ->")
print(l)