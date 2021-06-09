class Student:
    # instance attributes
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # instance method
    def check_pass_fail(self):
        if self.marks >= 40:
            return "Congratulation you have successfully passed"
        else:
            return "Better luck next time"

# instantiate the object
student1 = Student("Sam", 50)
# calling instance method
did_pass = student1.check_pass_fail()
print(did_pass)

student2 = Student('Harry', 30)
did_pass = student2.check_pass_fail()
print(did_pass)

#Output:
Congratulation you have successfully passed
Better luck next time

