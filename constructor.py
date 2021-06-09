class Student:
    """
    Returns a ```Student``` object with the given name, branch and year.

    """
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.") 

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year) 
        
# It will throw error missing 3 required postional arguments
#student1 = Student()

student1  = Student("Prasad" , "CSE", 4)
student1.print_details()

student2 = Student("Harry", "Civil", 3)
student2.print_details()

#Output:
A student object is created.
Name: Prasad
Branch: CSE
Year: 4
A student object is created.
Name: Harry
Branch: Civil
Year: 3
