# class Person:
#     name="mannu"
#     occupation="Software Developer"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a=Person()
# b=Person()
# a.name = "Shivam"
# a.occupation = "Accountant"



# b.name = "mannu"
# b.occupation = "software developer"

# a.info()
# b.info()

class Details:
    name = "Mannu Chaurasiya"
    age = 20
obj1 = Details()
print(obj1.name)
print(obj1.age)


# self :: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.


class Details:
    name = "mannu chaurasiya"
    age = "20"
    def desc(self) :
        print("the name of the employee is", self.name, " and his age is", self.age, "years old")
obj1 = Details()
obj1.desc()
