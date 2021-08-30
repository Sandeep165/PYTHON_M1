'''
Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable .count which counts the total number of instances created.

Examples
# Just finished writing the Composer class
Composer.count ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
Composer.count ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
Composer.count ➞ 3


Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not 
a vowel (like special characters or spaces), treat them like consonants.

Examples
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u

You are given a list of integers having both negative and positive values, except for one integer which can be negative or positive. 
Create a function to find out that integer.

Examples
lonely_integer([1, -1, 2, -2, 3]) ➞ 3
# 3 has no matching negative appearance.

lonely_integer([-3, 1, 2, 3, -1, -4, -2]) ➞ -4
# -4 has no matching positive appearance.

lonely_integer([-9, -105, -9, -9, -9, -9, 105]) ➞ -9


Create a function that takes a number as its parameter and returns another function. The returned function must take a list of numbers as its
 parameter,
and return a list of the numbers divided by the number that was passed into the first function.
first = factory(15)
# returns a function first.

lst = [30, 45, 60]
# 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4

first(lst) ➞ [2, 3, 4]
second = factory(2)
# returns a function second.

lst = [2, 4, 6]
# 2 / 2 = 1, 4 / 2 = 2, 6 / 2 = 3

second(lst) ➞ [1, 2, 3]

factory(int):
subFactory(lst)

'''

def factory(num):
    def subFactory(lst):
        return [ i//num for i in lst]
    return subFactory