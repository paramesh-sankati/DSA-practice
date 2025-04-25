class Academic:
    def __init__(self,grades,subjects):
        self.grades=grades
        self.subjects=subjects
    
class Extracurricular:
    def __init__(self,activities,awards):
        self.activities=activities
        self.awards=awards

class Student(Academic,Extracurricular):
    def __init__(self,grades,subjects,activities,awards):
        Academic.__init__(self,grades,subjects)
        Extracurricular.__init__(self,activities,awards)

obj1=Student('A',['maths','phy','tel'],'playing','CV Raman Award')
print(obj1.activities,obj1.awards,obj1.grades,obj1.subjects)