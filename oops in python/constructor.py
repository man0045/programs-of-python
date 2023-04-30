# class Person:

#     def __init__(self,n,o):
#         print("hey i am a person")
#         self.name=n
#         self.occ=o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=Person("mannu ","software Engineering")
# b=Person("harish ", "police officer")




# a.info()
# b.info()


# parameterized constructor

class Decode:
    def __init__(self,name , group):
        self.name= name
        self.group = group

obj1 = Decode( "rhinocorous", "animalia" )
print(obj1.name, "belongs to the", obj1.group, "group")


# default constructor
class decode1:
    def __init__(self):
        print("the name of the animal is dog and it is belongs to aimalia group")
obj1 =decode1()


