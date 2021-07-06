'''
Sum of Evenly Divisible Numbers from a Range
Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

def evenly_divisible(a,b,c):
    return sum([i for i in range(a,b+1) if i%c ==0])


print(evenly_divisible(1, 10, 2))
'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.  123==312

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
'''
def check_number(number):
    # num1 = str(number*2)
    # number = str(number)
    # count = 0
    # for i in number:
    #     if i in num1:
    #         count += 1
    #     else:
    #         return False
    #         break
    # if count == len(number):
    #     return True
    pass


def check_double(number):
    l1, l2 = list(str(number)), list(str(number * 2))
    return sorted(l1) == sorted(l2) and l1 != l2
