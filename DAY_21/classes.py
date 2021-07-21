'''
Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"



 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"

'''
# class player():
# 	def __init__(self, name, age, height, weight):
#             self.name=name
#             self.age=age
#             self.height=height
#             self.weight=weight

# p1 = player("David Jones", 25, 175, 75)
# print(p1.age)
# class player():
# 	def __init__(self, name, age, height, weight):
#             self.name=name
#             self.age=age
#             self.height=height
#             self.weight=weight
#     def get_age(self):
#             return '{} is age {}'.format(self.name,self.age)
#     def get_height(self):
#             return '{} is {} cm'.format(self.name,self.height)
#     def get_weight(self):
#             return '{} weighs {} kg'.format(self.name,self.weight)

# p1 = player("David Jones", 25, 175, 75)
# print(p1.get_age())



#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
    
#     def get_age(self):
#         s = self.name +" is age "+ str(self.age)
#         return s

#     def get_height(self):
#         s = self.name +" is "+ str(self.height)+" cm"
#         return s
    
#     def get_weight(self):
#         s = self.name +" weighs "+ str(self.weight)
#         return s


# player1 =  player("David Jones", 25, 175, 75)
# print(player1.get_age())
# print(player1.get_height())
# print(player1.get_weight())

class player():
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        
    def get_age(self):
        return f"{self.name} is age {self.age}" 

    def get_height(self):
        return f"{self.name} is {self.height}cm" 

    def get_weight(self):
        return f"{self.name} is {self.weight}kg" 

    def set_name(self,name1):
        self.name = name1
        return f"{self.name} " 


p1 = player("David Jones", 25, 175, 75)

# print(p1.get_age())
# print(p1.get_height())
print(p1.name)
print(p1.set_name("Harry"))
print(p1.name)
# getter/setter------------->get the value and writes the results/set the value and writes the result
'''
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

Population density is calculated by dividing the population by the area.
Area is given in square km.
The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.
'''
# p = int(input(""))
# a = int(input(""))
# is_big = p>250*10**6 or a>3*10**6


# is_big = False
# if p>250*10**6 or a>3*10**6:
#     is_big = True


# if p>250*10**6 or a>3*10**6:
#     is_big = True
# else:
#     is_big =False

# class Country:

# 	def __init__(self, name, population, area):
# 		self.name = name
# 		self.population = population
# 		self.area = area
# 		# implement self.is_big
# 		self.is_big = population>250*10**6 or area>3*10**6 

#     def compare_pd(self,other):
# 		if self.population/self.area > other.population/other.area:
#             return f"{self.name} has a larger population density than {other.name}"
#         else:
#             return f"{self.name} has a smaller population density than {other.name}"

    
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)


class Country:

	def __init__(self, name, population, area):
		self.name = name
		self.population = population
		self.area = area

		if self.population > 250000000 or self.area > 3000000:
			self.is_big = True
		else:
			self.is_big = False
		
	def compare_pd(self, other):

		if (self.population / self.area) > (other.population / other.area):
			return(self.name + " has a larger population density than " + other.name)
		else:
			return(self.name + " has a smaller population density than " + other.name)

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.is_big)

print(andorra.compare_pd(australia))