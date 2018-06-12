#question1
i=0
emptylist=[]
while i<=4:
    val = int(input("ENTER THE VALUE"))
    emptylist.append(val)
    i=i+1
print(emptylist)

#question2

while True:
   print("***")

#question3
i=0
emptylist=[]
while i<=4:
    val = int(input("ENTER THE VALUE"))
    emptylist.append(val)
    i=i+1
print(emptylist)
i=0
while i<=4:
    print("SQUARE OF ELEMENTS--> %d"%(emptylist[i]*emptylist[i]))
    i = i + 1


#question 4
a=[]
il=[]
fl=[]
sl=[]
b=[]
i=0
while i<=4:
    val =input("ENTER THE VALUE IN LIST")
    a.append(val)
    i=i+1
print(a)

i=0
while i<=4:
    val = type(a[i])
    #print (val)
    b.append(val)
    i=i+1
print(b)

i=0
while i<=4:
    b[i]=str(b[i])
    #print(type(b[i]))
    if 'str' in b[i]:
        sl.append(a[i])
    if 'int' in b[i]:
        il.append(a[i])
    if 'float' in b[i]:
        fl.append(a[i])
    else :
        print("TYPE NOT FOUND")
    i = i + 1
print("INTEGER LIST")
print(il)
print("STRING LIST")
print(sl)
print("FLOAT LIST")
print(fl)

#question5
odd=[]
even=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

#question6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()


#question7
d={'name':'AYUSHMAT','age':20,'city':'Shimla','COLLEGE':'JUIT'}
for i in d:
    print(d[i])
print(dict.keys(d))
print(dict.items(d))

#question8
a=[]
i=0
while i<=4:
   num=int(input("ENTER THE VALUE"))
   a.append(num)
   i+=1

print(a)
i=0

s=int(input("ENTER THE VALUE YOU WANT TO DELETE"))
if s in a:
    a.remove(s)
    print("ElEMENT REMOVED!")
else:
    print("ELEMENT NOT FOUND")
print(a)
