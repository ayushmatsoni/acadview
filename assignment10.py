#question1

class Circle:
    #r=int(input("ENTER THE RADIUS"))
    def getArea(self,r):
        ar=3.14*r*r
        print("Area = %.2f"%(ar))
        return 0
    def getCircumference(self,r):
        cir=3.14*2*r
        print("Circumference = %.2f"%(cir))
        return 0
r=int(input("ENTER THE RADIUS"))
x=Circle()
ch=int(input("ENTER YOUR CHOICE (1/2)"))
if ch == 1 :
    x.getArea(r)
elif ch == 2 :
    x.getCircumference(r)
else:
    print("Wrong Choice")


#question2
class Student:
    def display(self,name,rn):
        print(name)
        print(rn)
name=input("ENTER THE NAME")
rn=input("ENTER THE ROLL NUMBER")
y=Student()
y.display(name,rn)


#question3
fer=0
cel=0



class Temprature:
    def convertC2F(self,c):
        fer=(9/5)*c+32
        print("TEMP IN F %.2f"%(fer))
        return 0
    def convertF2C(self,f):
        cel=(5/9)*(f-32)
        print("TEMP IN c %.2f"%(cel))
        return 0
z=Temprature()
print("1 for celsius into farenhiet")
print("2 for farenhiet into celsius")
ch2=int(input("ENTER YOUR CHOICE (1/2)"))
if ch2 == 1:
    print("enter temp in celsius")
    c=int(input())
    z.convertC2F(c)
elif ch2 == 2:
    print("enter temp in farenhiet")
    f = int(input())
    z.convertF2C(f)
else:
    print("Wrong Choice")
print("")


#question4
mn=""
an=""
yor=""
rat=0
mn=input("ENTER MOVIE NAME")
an=input("ENTER ARTIST NAME")
yor=input("ENTER YEAR OF RELEASE")
rat=int(input("ENTER RATINGS"))

class MovieDetails :
    def displaydetails(self,mn,an,yor,rat):
        print("MOVIE NAME"+mn)
        print("ARTIST NAME" + an)
        print("YEAR OF RELEASE" + yor)
        print("RATINGS %d"%(rat))
    def updatedetails(self,mn,an,yor,rat):
        mn = input("ENTER MOVIE NAME ")
        an = input("ENTER ARTIST NAME " )
        yor = input("ENTER YEAR OF RELEASE ")
        rat = int(input("ENTER RATINGS "))

        print("NEW MOVIE NAME " + mn)
        print("NEW ARTIST NAME " + an)
        print("NEW YEAR OF RELEASE " + yor)
        print("NEW RATINGS%d" % (rat))

zz=MovieDetails()
print("1 for display details")
print("2 for update details")
ch3=int(input("ENTER YOUR CHOICE (1/2)"))

if ch3 == 1:
    print("DETAILS->")
    #inputfn()
    zz.displaydetails(mn,an,yor,rat)
elif ch3 == 2:
    print("UPDATED DETAILS->")
    #inputfn()
    zz.updatedetails(mn,an,yor,rat)
else:
    print("Wrong Choice")


#question5
exp=0
sav=0
sal=0
s=0
class Expenditure:
    def displayresult(self, exp,sav):
        print("EXPENDITURE -->%.2f"%(exp))
        print("SAVINGS-->%.2f"%(sav))
        print("")
    def calculateresult(self, exp,sav):
        sal=exp+sav
        return sal
    def displaysalary(self,s):
        print("TOTAL SALARY -->%.2f" % (s))

exp = int(input("ENTER THE EXPENDITURE"))
sav = int(input("ENTER THE SAVINGS"))
zzz = Expenditure()
zzz.displayresult(exp,sav)
zzz.calculateresult(exp,sav)
s=zzz.calculateresult(exp,sav)
zzz.displaysalary(s)
