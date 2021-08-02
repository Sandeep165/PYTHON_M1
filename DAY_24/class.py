
'''

Given a list of people objects, create a function that sorts the list by an attribute name. 
The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

firstname
lastname
age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40











Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.

Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6

is_equal([21, 35]) ➞ False

is_equal([0, 0]) ➞ True






In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
Notes
Keep the same ordering in the output.


'''
# class Person:
#     def __init__(self, firstname, lastname, age):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age
#     def people_sort(self,lst, attr):
#         return sorted(lst.firstname) if attr=="firstname" else sorted(lst.lastname) if attr=="lastname" else sorted(lst.age)
# p1 = Person("Michael", "Smith", 40)
# p2 = Person("Alice", "Waters", 21)
# p3 = Person("Zoey", "Jones", 29)

# print(people_sort([p1, p2, p3], "firstname"))

def return_unique(lst):
    return [k for k in lst if lst.count(k)==1]
print(return_unique([1,1,2,3,3,4,5,5]))


'''

Given two strings, return a string containing only the letters shared between the two.

Examples
shared_letters("house", "home") ➞ "eho"

shared_letters("Micky", "mouse") ➞ "m"

shared_letters("house", "villa") ➞ ""
Notes
If none of the letters are shared, return an empty string.
The function should be case insensitive (e.g. comparing A and a should return a).
Sort the resulting string alphabetically before returning it.


Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

Examples
oddish_or_evenish(43) ➞ "Oddish"
# 4 + 3 = 7
# 7 % 2 = 1

oddish_or_evenish(373) ➞ "Oddish"
# 3 + 7 + 3 = 13
# 13 % 2 = 1

oddish_or_evenish(4433) ➞ "Evenish"
# 4 + 4 + 3 + 3 = 14
# 14 % 2 = 0

'''
