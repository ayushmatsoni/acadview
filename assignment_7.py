import numpy as np

#question1
ar= np.random.rand(10,1)
print("10*1 Array=")
print(ar)
mn=np.mean(ar)
print("MEAN=")
print(mn)
print()
#question2
ar2= np.random.rand(20,1)
print("20*1 Array=")
print(ar2)
sd=np.std(ar2)
print("Standard Deviation=")
print(sd)

vr=np.var(ar2)
print("Variance=")
print(vr)
print()

#question3
ar3= np.random.rand(10,20)
ar4= np.random.rand(20,25)
print(ar3)
print(ar4)
print("AxB=")
print(np.matmul(ar3,ar4))
print("SUM OF ELEMENTS=")
print(np.sum(np.matmul(ar3,ar4)))

#question4
ar5= np.random.rand(10,1)
ar6=1/(1+np.exp(-(ar5)))
print()
print("10x1 array=")
print(ar5)

print()
print("10x1 array after operation f(x)=")
print(ar6)