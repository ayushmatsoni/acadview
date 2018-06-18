#QUESTION1
class Animal:
    def animal_attribute(self):
        print('''THIS IS "animal_attribute" function of "Animal" class.''')
        print("")
class Tiger(Animal):
    def tiger_attribute(self):
        print('''THIS IS "tiger_attribute" function of "Tiger" inherited-class.''')
        print("")
obj=Tiger()
obj.animal_attribute()
obj.tiger_attribute()

#QUESTION2
#AB
#AB


#QUESTION3
class Cop:
    def __init__(self,name,age,workexp,desg):
        self.name=name
        self.age=age
        self.workexp = workexp
        self.desg = desg

    @classmethod
    def add(cls):
        cls.name=input("ENTER THE NAME")
        cls.age=int(input("ENTER THE AGE"))
        cls.workexp=int(input("ENTER THE WORK EXPERIENCE"))
        cls.desg=input("ENTER THE DESIGNATION")
        return Cop(cls.name,cls.age,cls.workexp,cls.desg)

    @classmethod
    def display(cls):
        print("DETAILS OF EMPLOYEE ARE-->")
        print("NAME-> "+cls.name)
        print("AGE-> %d"%cls.age)
        print("WORK EXPERIENCE--> %d" %cls.workexp)
        print("DESIGNATION-->"+cls.desg)

    def update(self):
        print("UPDATE DETAILS-->")
        self.add()
        self.display()

obj1=Cop("ayush",21,5,"stu")
obj1.add()
obj1.display()
ch=input("DO YOU WANT TO UPDATE THE DETAILS?(Y/N)")
if ch=='y' or ch=='Y':
    obj1.update()


#QUESTION4

class Shape:
    def __init(self,len,bre):
        self.len=len
        self.bre=bre
class Square(Shape):
    def area(self,len):
        return len*len
class Reactangle(Shape):
    def area(self,len,bre):
        return len*bre

objj=Shape()
objj1=Square()
objj2=Reactangle()
len=int(input("Enter the length"))
bre=int(input("Enter the breadth"))
print("AREA OF SQUARE = ",(objj1.area(len)))
print("AREA OF REACTAGLE = ",(objj2.area(len,bre)))
#print(objj2.area(len,bre))