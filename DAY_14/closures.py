
# Python program to illustrate
# nested functions
# def outer(func):
        # global
#     def inner(a,b):
#         print("-------------------*----------------------")
#         print("-------------------*----------------------")
#         func(a,b)  #3
#         print("-------------------*----------------------")
#         print("-------------------*----------------------")        
#     return inner


# @outer
# def sum(a,b):
#     print(a+b)

# sum(1,2)
def print_msg(message):
    greeting = "Good Morning..."  #non local var(global var)

    def printer():
        print(greeting,message)

    return printer

res = print_msg("Students !")

res()
# 
# letter
letters = ["a","b","c","d","e","i","u","z"]

# def my_vowel(letter):
#     vow = ["a","e","i","o","u"]
#     if letter in vow:
#         return True
#     else:
#         return False 

# vowels = list(filter(lambda x: x in ["a","e","i","o","u"] ,["a","b","c","d","e","i","u","z"]))
# print(vowels)
# # for i in vowels:
# #     print(i)

# # vowels = [a,e,i,o,u]
# numbers = [-2, -1, 0, 1, 2]

# positive=list(filter(lambda x: x>0 ,numbers))
# print(positive)
import math

# print(math.pow(10,2))
'''

Method	Description
math.acos()	        Returns the arc cosine of a number
math.acosh()	    Returns the inverse hyperbolic cosine of a number
math.asin()	        Returns the arc sine of a number
math.asinh()	    Returns the inverse hyperbolic sine of a number
math.atan()     	Returns the arc tangent of a number in radians
math.atan2()    	Returns the arc tangent of y/x in radians
math.atanh()	    Returns the inverse hyperbolic tangent of a number
math.ceil()	          Rounds a number up to the nearest integer
math.comb()	        Returns the number of ways to choose k items from n items without repetition and order
math.copysign()	    Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()      	Returns the cosine of a number
math.cosh()	        Returns the hyperbolic cosine of a number
math.degrees()  	Converts an angle from radians to degrees
math.dist()	        Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()	           Returns the error function of a number
math.erfc()     	Returns the complementary error function of a number
math.exp()	    Returns E raised to the power of x
math.expm1()	Returns Ex - 1
math.fabs()	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor()	Rounds a number down to the nearest integer
math.fmod()	Returns the remainder of x/y
math.frexp()	Returns the mantissa and the exponent, of a specified number
math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()	Returns the gamma function at x
math.gcd()	Returns the greatest common divisor of two integers
math.hypot()	Returns the Euclidean norm
math.isclose()	Checks whether two values are close to each other, or not
math.isfinite()	Checks whether a number is finite or not
math.isinf()	Checks whether a number is infinite or not
math.isnan()	Checks whether a value is NaN (not a number) or not
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()	Returns the log gamma value of x
math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()	Returns the base-10 logarithm of x
math.log1p()	Returns the natural logarithm of 1+x
math.log2()	Returns the base-2 logarithm of x
math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
math.pow()	Returns the value of x to the power of y
math.prod()	Returns the product of all the elements in an iterable
math.radians()	Converts a degree value into radians
math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
math.sin()	Returns the sine of a number
math.sinh()	Returns the hyperbolic sine of a number
math.sqrt()	Returns the square root of a number
math.tan()	Returns the tangent of a number
math.tanh()	Returns the hyperbolic tangent of a number
math.trunc()	Returns the truncated integer parts of a number
'''
'''
function(a,b,c)
ax**2 + bx + c = 0
x/-x = -b+-sqrt(b^2-4ac)/2a
6x² + 11x - 35 = 0.

'''
# import math
# def eqn(a, b, c):
#     sol1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     sol2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     return sol1, sol2
# print(eqn(6,11,-35))


def eqn(a, b, c):
    sol1 = (-b + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
    sol2 = (-b - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
    return sol1, sol2


print(eqn(6, 11, -35))
