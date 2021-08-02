# Python program to demonstrate
# multiple inheritance
 
 
# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

'''Question'''

'''create classes person and company to get the details of the respective and derive employee class to get the employee details of that person 
person - name,age
company - company_name,location
'''
'''solution'''
class Person:
    name=""
    age=1
    def person(self):
        print(f"name is {self.name} age is {self.age}")
class Company:
    company_name=""
    loc=""
    def company(self):
        print(f"company name is {self.company_name} location is {self.loc}")
class Employee(Person,Company):
    def employee(self):
        print(f"name is {self.name}, age is {self.age}")
        print(f"company name is {self.company_name}, location is {self.loc}")

e1= Employee()
e1.name="akash"
e1.age=20
e1.company_name="TCS"
e1.loc="malad"
e1.employee()
