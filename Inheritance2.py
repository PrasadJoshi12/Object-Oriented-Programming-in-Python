class Person:
    def __init__(self, name):
        self.name = name
    def get_details(self):
        return self.name

class Teacher(Person):
    def __init__(self, name, subjects):
        super().__init__(name)
        self.subjects = subjects
    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.subjects))
class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year
    def get_details(self):
        return "{} is studying in {} year".format(self.name, self.year)


person1 = Person('Harry')
print(person1.get_details())
        
teacher1 = Teacher("Sam", ["C", "Python"])
print(teacher1.get_details())

student1 = Student("Gary", "Second")
print(student1.get_details())

#Output:
Harry
Sam teaches C,Python
Gary is studying in Second year

    
