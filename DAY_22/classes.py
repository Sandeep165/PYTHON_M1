# class Country:

# 	def __init__(self, name, population, area):
# 		self.name = name
# 		self.population = population
# 		self.area = area

# 		if self.population > 250000000 or self.area > 3000000:
# 			self.is_big = True
# 		else:
# 			self.is_big = False

# 	def compare_pd(self, other):

# 		if (self.population / self.area) > (other.population / other.area):
# 			return(self.name + " has a larger population density than " + other.name)
# 		else:
# 			return(self.name + " has a smaller population density than " + other.name)

# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)
# print(australia.is_big)

# print(andorra.is_big)

# print(andorra.compare_pd(australia))

'''

Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
Name the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:
Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
'''


# class Book:

#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def get_title(self):
#         return "Title: " + self.title

#     def get_author(self):
#         return "Author: " + self.author


# PP = Book('Pride and Prejudice', 'Jane Austen')
# H = Book('Hamlet', 'William Shakespeare')
# WP = Book('War and Peace', 'Leo Tolstoy')


'''
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.

Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

https://edabit.com/challenge/iRvRtg2xxL9BnSEvf

'''
# class Person():
#     def __init__(self,name,like,hate):
#         self.name=name
#         self.like=like
#         self.hate=hate
#     def taste(self,f_name):
#         if f_name in self.like:
#                 return self.name+ " eats the "+ f_name +" and loves it!"
#         elif f_name in self.hate:
#                 return self.name+ " eats the "+ f_name +" and hates it!"
#         else:
#                 return self.name+ " eats the "+ f_name +" !"


# class Person:
#     def __init__(self,name,love,hate):
#         self.name = name
#         self.love = love
#         self.hate = hate
#     def taste(self,food_name):
#         if food_name in self.love:
#             return self.name+" eats the "+food_name+" and loves it!"
#         elif food_name in self.hate:
#             return self.name+" eats the "+food_name+" and hates it!"
#         else:
#             return self.name+" eats the "+food_name+"!"

# class Person:
#     def __init__(self,name,like,hate):
#         self.name=name
#         self.like=like
#         self.hate=hate
#     def taste(self,food):
#         if food in self.like:
#             return "{} eats the {} and loves it!".format(self.name,food)
#         elif food in self.hate:
#             return "{} eats the {} and hates it!".format(self.name,food)
#         else:
#             return "{} eats the {}!".format(self.name,food)

# class person:


#     def __init__(self, name, like, hate):
#         self.name = name
#         self.like = like
#         self.hate = hate


#         def taste(self, food):
#                  if food in self.like:
#                         ext = "and loves it!"
#                  elif food in self.hate:
#                         ext = "and hates it!"
#                  else:
#                           ext = "!"
#                  return f"{self.name} eats {food}  {ext}"


# a = person("John", ["pizza", "burger"], ["carrots"])

# print(a.taste("burgers"))


# p1 = Person("Sam", ["ice cream"], ["carrots"])
# print(p1.taste("ice cream"))

# print(p1.taste("cheese"))

# print(p1.taste("carrots"))


# class employee:
#     emp_count = 0 #class variable

#     def __init__(self, e_name):
#         self.e_name = e_name  #instance var
#         employee.emp_count += 1
#         print("I am constructor")

# e1 = employee("Harry")
# e2 = employee("Same")
# print(e1.emp_count)
# print(e2.emp_count)
#
'''

Create a class named User and create a way to check the number of users (number of instances) were created,
 so that the value can be accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"

'''




'''


Create a method in the Person class which returns how another person's age compares.
Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:

{other_person} is {older than / younger than / the same age as} me.

Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2) ➞ "Joel is older than me."

p2.compare_age(p1) ➞ "Samuel is younger than me."

p1.compare_age(p3) ➞ "Lily is the same age as me."


'''


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare_age(self,other):
        if self.age > other.age:
            return other.name+" is younger than me."
        elif self.age == other.age:
            return other.name+" is the same age as me."
        else:
            return other.name+" is older than me."
p1 = person("Samuel", 24)
p2 = person("Joel", 36)
p3 = person("Lily", 24)
print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))
