#Counting the number of object.
class Student:
    count = 0
    def __init__(self):
        Student.count += 1
    def display(self):
        return self.count

student1 = Student()
student2 = Student()
student3 = Student()

print(Student.count)

#Output:
3
