'''
We have a base class Person that stores general information like name and age. We then have multiple derived classes that represent different types of students, like UndergraduateStudent and GraduateStudent, which both inherit from the Person class.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class UndergraduateStudent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
class GraduateStudent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

ug=UndergraduateStudent('hari',23)
g=GraduateStudent('abhi',21)
print(ug.name,ug.age)
print(g.name,g.age)