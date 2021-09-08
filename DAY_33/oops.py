'''
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        print(max speed)

'''


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        print(self.max_speed)

class Bus(Vehicle):

    def show(self):
        print("I am from class Bus")


'''
class bus(vehicle)............set var bus_name,  bus_state, bus_status
class bus1(bus)...........def speed......def info(bus_name, bus_status, bus_state)

'''

obj1 = Bus("Tata",55,35)
print(obj1.name)
print(obj1.max_speed)
print(obj1.mileage)
print(obj1.show())
obj1.speed()

'''
Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

'''
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class bus(Vehicle):
    def seating_capacity(self, capacity = 50 ):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        print(self.max_speed)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,bus_name,bus_state,bus_status):
        super().__init__(name, max_speed, mileage)
        self.bus_name=bus_name
        self.bus_state=bus_state
        self.bus_status=bus_status

class Bus1(Bus):
    def info(self):
        print(f"name: {self.bus_name}, state: {self.bus_state}, status:{self.bus_status}")
    
obj=Bus1("car1",55, 35,"B101","malad","active")
print(obj.bus_name)
print(obj.name)
obj.speed()
obj.info()



'''


The 50-30-20 strategy is a simple way to budget, which involves spending 50% of after-tax income on needs, 30% after tax income on wants,
 and 20% after-tax income on savings or paying off debt.

Given the after-tax income as ati, what you are supposed to do is to make a function that will return a dictionary that shows how much a
 person needs to spend on needs, wants, and savings.

Examples
fifty_thirty_twenty(10000) ➞ { "Needs": 5000, "Wants": 3000, "Savings": 2000 }

fifty_thirty_twenty(50000) ➞ { "Needs": 25000, "Wants": 15000, "Savings": 10000 }

fifty_thirty_twenty(13450) ➞ { "Needs": 6725, "Wants": 4035, "Savings": 2690 }


return {
    "Needs" : 20,
    "wants" : 50,
    "Saving" : 30
 }

'''

def fifty_thirty_twenty(ati):   #50%.......50/100.....1/2...0.5
    # return{ 
    #     "Needs": ati * 0.5, 
    #     "Wants": ati*0.3 , 
    #     "Savings": ati*0.2
    #      }

    # keys = ["Needs","Wants","Saving"]
    # values = [(ati*0.5), (ati*0.3), (ati*0.2)]

    # return dict(zip(keys,values))

    dict1 = {}
    dict1["Needs"] = 0.5*ati
    dict1["Wants"] = 0.3*ati
    dict1["Values"] = 0.2*ati
    

'''
Write a function that returns True if a dictionary contains the specified key, and False otherwise.

Examples
has_key({ "a": 44, "b": 45, "c": 46 }, "d") ➞ False

has_key({ "craves": True, "midnight": True, "snack": True }, "morning") ➞ False

has_key({ "pot": 1, "tot": 2, "not": 3 }, "not") ➞ True



'''