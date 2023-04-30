class parent:
    def func1(self):
        print("this function is an parent class. ")

class child(parent):
    def func2(self):
        print("this function is in child class. ")

object = child()
object.func1()
object.func2()


#multiple Inheritance:
# When a class can be derived from more 
# than one base class this type of inheritance is called multiple inheritances. 
# In multiple inheritances, all the features of the base 
# classes are inherited into the derived class.


class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class son(Mother, Father):
    def parents(self):
        print("father name is :", self.fathername)
        print("Mother : ", self.mothername)
s1 = son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"

s1.parents()


# Multilevel Inheritance :
# In multilevel inheritance, features of the base class 
# and the derived class are further inherited into the new derived class. This is similar to a 
# relationship representing a child and a grandfather.
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Pania lal', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type
#  of inheritance is called hierarchical inheritance. 
# In this program, we have a parent (base) class and two child (derived) classes.

class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()