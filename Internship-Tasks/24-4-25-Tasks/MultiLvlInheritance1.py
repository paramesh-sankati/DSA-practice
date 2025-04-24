'''
We want to model a system where we have a base class for Person that contains basic information (like name and age). Then, we have a Student class that inherits from Person and adds information about the student's roll_number and grades. Finally, we have a GraduateStudent class that inherits from Student and adds additional attributes like the degree they are pursuing.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,rno,grades):
        super().__init__(name,age)
        self.rno=rno
        self.grades=grades
class GraduateStudent(Student):
    def __init__(self,name,age,rno,grades,degree):
        super().__init__(name,age,rno,grades)
        self.degree=degree

obj=GraduateStudent('param',21,101,'A','Btech')
print(obj.name,obj.age,obj.rno,obj.grades,obj.degree)



        