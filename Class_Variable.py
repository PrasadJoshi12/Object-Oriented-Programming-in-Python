class Car:
    # class/static variable
    wheels = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def print_values(self):
        print(self.name)
        print(self.color)
        print(self.wheels)

car1 = Car('Volwo' , 'Blue')
car1.print_values()
# wheels value will be get changed for all the objects.
Car.wheels = 5

car2 = Car('Toyota' , 'Red')
car2.print_values()

car3 = Car("Safari" , "Black")
car3.print_values()

#Output:
Volwo
Blue
4
Toyota
Red
5
Safari
Black
5

