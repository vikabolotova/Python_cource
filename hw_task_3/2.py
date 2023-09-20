class Student:

    def __init__(self):
        self.knowledge = []


    def take(self,subject):
        self.knowledge.append(subject)


class Teacher:
    def __init__(self):
        self.num_stud = 0

    def teach(self, subject, *students):
        for student in students:
            student.take(subject)
        self.num_stud = self.num_stud + 1


class StudyMaterials:

    def __init__(self,*subjects):
        self.subjects = list(subjects)


mat = StudyMaterials("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher()

stud1 = Student()
stud2 = Student()
stud3 = Student()
stud4 = Student()

teacher.teach(mat.subjects[0], stud1, stud2, stud3)
teacher.teach(mat.subjects[1], stud4, stud1, stud2)
teacher.teach(mat.subjects[2], stud3, stud4, stud1)
teacher.teach(mat.subjects[3], stud2, stud3, stud4)
teacher.teach(mat.subjects[4], stud1, stud4, stud3)


print(stud1.knowledge)
print(stud2.knowledge)
print(stud3.knowledge)
print(stud4.knowledge)