import random
class Person:

    def __init__(self, last_name, age, sex):
        self.last_name = last_name
        self.age = age
        self.sex = sex


class Student(Person):

    def __init__(self, last_name, age, sex):
        self.knowledge = []
        super().__init__(last_name, age, sex)

    def __len__(self):
        return len(self.knowledge)

    def take(self,subject):
        self.knowledge.append(subject)


    def forget_knowledge(self, num_elements):
        print(num_elements)
        for _ in range(num_elements):
            print(_)
            index = random.randint(0, len(self.knowledge) - 1)
            print(f"index: {index}")
            self.knowledge.pop(index)

class Teacher(Person):

    def __init__(self, last_name, age, sex):
        self.num_stud = 0
        super().__init__(last_name, age, sex)

    def teach(self, subject, *students):
        for student in students:
            student.take(subject)
        self.num_stud = self.num_stud + 1


class StudyMaterials:

    def __init__(self,*subjects):
        self.subjects = list(subjects)

    def __len__(self):
        return len(self.subjects)






mat = StudyMaterials("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher("Иванова Людмила Александровна", 47, "ж")

stud1 = Student("Петров", 10, "м")
stud2 = Student("Сидоров", 15, "м")
stud3 = Student("Тимошенко", 13, "ж")
stud4 = Student("Александрова", 14, "ж")


teacher.teach(mat.subjects[0], stud1, stud2, stud3)
teacher.teach(mat.subjects[1], stud4, stud1, stud2)
teacher.teach(mat.subjects[2], stud3, stud4, stud1)
teacher.teach(mat.subjects[3], stud2, stud3, stud4)
teacher.teach(mat.subjects[4], stud1, stud4, stud3)

stud4.forget_knowledge(2)


print(stud1.knowledge)
print(stud2.knowledge)
print(stud3.knowledge)
print(stud4.knowledge)