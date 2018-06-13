#QUESTION 1

ar=1
r=int(input("ENTER THE RADIUS"))
def area (r):
    ar=3.14*r*r
    return ar
print(area(r))

#QUESTION 2

i=0
sum=0
def perfect():
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j;

        if sum==i:
            print("%d"%(i))
    return 0
print("THE PERFECT NO.S ARE-->")
perfect()


#QUESTION 3
l=int(input("ENTER THE LIMIT"))
def table(l,):
     if l==1:
         ans=12*1
         return print(ans)
     else:
         table(l-1)
         ans= (12*l)
         print("TABLE VALUES-->")
         return print(ans)
print(table(l))


#QUESTION 4

result=1
a=int(input("ENTER THE NUMBER"))
b=int(input("ENTER THE POWER"))

def power(a,b):
    if b!=0:
        return (a*power(a,b-1))
    else:
        return 1
result=power(a,b)
print("Answer =%.4f"%(result))


#QUESTION 5

n=int(input("ENTER THE LIMIT"))
def fact(n):
    if n==1:
       return 1
    else :
        return (n * fact(n - 1))

dict={'number':n,'Factorial':fact(n)}
print(fact(n))
print(dict)
