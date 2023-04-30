# Access specifiers or access modifiers in python programming are used to limit the access
# of class variables and class methods outside of class while implementing the concepts of
#  inheritance.

# there are three types of Access modifier in oops concept of python
# which is 
# 1> PUBLIC Modifier
# 2> Private Modifier
# 3> Protected Modifier

# 1 > public Modifier
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
# All the variables and methods (member functions) in python are by default public. 
# Any instance variable in a class followedby the ‘self’ keyword ie. self.var_name are 
# public accessed.

# 2>> private Modifier

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

print(obj.__age)
print(obj.__funName())
print(obj1.__age)
print(obj1.__funName())
# all the variables and methods (member function ) in python are use in any particula block.
# and used privately

#3 >> protected Modifier
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

# Example:




