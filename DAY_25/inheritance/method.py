class Parent:
    def func1(self):
        print("this is parent function")
 
class Child(Parent):
    def func1(self):
        print("this is child function")
 
ob = Child()
ob.func1()