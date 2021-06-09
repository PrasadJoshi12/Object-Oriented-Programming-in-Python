# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):
    def __init__(self):
        # calling parents init method
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim() # It will print swim faster
peggy.run()



#Output:
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
