'''

Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"
Notes
If any input is "" or None, return "Invalid Operation".



A built-in timer inside your car can count the length of your ride in minutes and you have started your ride at 00:00  #hr:min = 05:24 = 0+5+2+4.

Given the number of minutes n at the end of the ride, calculate the current time. Return the sum of digits that the digital timer in the format hh:mm will show at the end of the ride.

Examples
car_timer(240) ➞ 4  = 04:00 = 0+4+0+0
# 240 minutes have passed since 00:00, the current time is 04:00
# Digits sum up is 0 + 4 + 0 + 0 = 4

car_timer(808) ➞ 14 = hr:min = h+r+m+n =

car_timer(14) ➞ 5




Create a function (named fifth) that takes some arguments and returns the type of the fifth argument. In case the arguments were less than 5, return "Not enough arguments".

Examples
fifth(1, 2, 3, 4, 5) ➞ int

fifth("a", 2, 3, [1, 2, 3], "five") ➞ str

fifth() ➞ "Not enough arguments"



Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1

'''


# class find:
#     def __init__(self,n1):

#         self.nines = n1//9

#         self.ones = n1//1

#         self.threes = n1//3

# obj1 = find(13)
# print(obj1.ones)
# print(obj1.threes)
# print(obj1.nines)
class ones_threes_nines:

    def __init__(self, n):
        self.n = n

    def ones(self):
        return self.n//1

    def threes(self):
        return self.n//3

    def nines(self):
        return self.n//9

    def display(self):
        return "hello"


obj1 = ones_threes_nines(13)
print(obj1.ones())
print(obj1.threes())
print(obj1.nines())


