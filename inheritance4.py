# Inheritance
# Hierachical Inheritance
class Animal:
    """
    Represents animal
    """
    sound = ""
    def __init__(self, name):
        """
        name:
            The name of the animal
        """
        self.name = name
    
    def speak(self):
        """
        Print's the name and sound of the animal.
        """
        print("{} speaks {}".format(self.name, self.sound))

class Piglet(Animal):
    sound = "ook ook"

class Cow(Animal):
    sound = "Moooooo"

pig = Piglet("xyz")
pig.speak()

cow1 = Cow("abc")
cow1.speak()


#Output:
#xyz speaks ook ook
#abc speaks Moooooo
