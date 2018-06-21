#question1
print("QUESTION 1")
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("THIS IS ZERO DIVISION ERROR")

print("")
print("QUESTION2")
#question2
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("THIS IS INDEX ERROR")

print("")
print("QUESTION3")
#question3
print("'AN EXCEPTION'")

print("")
print("QUESTION4")
#question4
print(-5.0)
print("a/b result is 0")

print("")
print("QUESTION5")
#question5


try :
    import HELLO

except ImportError:
    print("THIS IS IMPORT ERROR")
    pass

try:
    n=int(input("ENTER ANY NUMBER"))
except ValueError:
    print("THIS IS VALUE ERROR")
    pass
else:
    print(n)
try:
    x=[1,2,3]
    i=int(input("ENTER ANY INDEX"))
    print(x[i])
except IndexError:
    print("THIS IS INDEX ERROR")


print("")
print("QUESTION6")
#question6

class AgeTooSmallError(Exception):
    pass
a=0
while a<18:
    try:
        a = int(input("ENTER AGE"))

        if a<18:
                raise AgeTooSmallError
                pass
        else :
            print(a)
    except:
        print("AGE LESS THAN 18 ")
        print("try again")

