# A Python program to demonstrate inheritance 
  
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"
class Base(object):
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
  
# Python program to demonstrate
# multilevel inheritance
 
# Base class
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
# Derived class
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()