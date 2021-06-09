class Person:
    def __init__(self, name):
        self.__name = name
    
    def get_details(self):
        return "This is {}".format(self.__name)

class Child(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def tell(self):
        return "This is {}".format(self.__name)

c = Child("Sam")
print(c.get_details())

# tell method will throw an error object has no attribute __name.
#print(c.tell())

p = Person("Harry")
print(p.get_details())

# Output:
This is Sam
This is Harry
