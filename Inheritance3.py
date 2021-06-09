class A:
    def method1(self):
        print("In method1 of class A")
    def method2(self):
        print("In method2 of class A")

class B:
    def method2(self):
        print("In method2 of class B")
    def method3(self):
        print("In method3 of class B")


# Multiple Inheritance
class C(B, A):
    def method4(self):
        print("In method4 of class C")

# Create object of class C
obj = C()
obj.method1()
# It will print method2 of class B because of MRO(Method Resolution Order)
obj.method2() 
obj.method4()


#Output:
In method1 of class A
In method2 of class B
In method4 of class C
