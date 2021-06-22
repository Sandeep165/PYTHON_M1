square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
new_dict = square

new_dict.popitem()
print(square)

# Python conditional statement

'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''

num1 = 100
num2 = 200
# if (num1>num2):
#     print("num1 is greater than num 2")
# else:
#     print("num1 is less than num2")


# age=int(input("enter age:"))

# if age<=0:
#     print("invalid age")
# elif 0<age>18:
#     print("not eligible")
# else:
#     print("eligible")


# and
'''
T F F
T T T
F F F
F T F
'''

# OR
'''
T T T
T F T
F T T
F F F
'''

# NOT
'''
T F
F T
'''


A = 10
B = 15
C = 20

# if A > B & A > C:
#     print("A is the largest no.")
# elif B > A & B > C:
#     print("B is the largest no.")
# else:
#     print("C is the largest no.")

# A>B A>C.......B>A B>C......C


val = 25
if val > 20:
    print("greater than 20")
    if val > 21:
        print("and greater than 21")
    else:
        print("not above 21")
num = 25

if num != 0:
    pass

num = 15
# if num % 5 == 0:
#     print("divisible by 5")


# num div 3 and 5  star
# num div 4 and 5  circle
# "pass"
num = 28
# if(num%3 == 0 and num%5 == 0):
#     print("Star")
# elif(num%4 == 0 and num%5 ==0):
#     print("Circle")
# else:
#     print("pass")

num = 35
if num % 5 == 0:
    print("divisible by 5")
    if num % 3 == 0:
        print("star")
    if num % 4 == 0:
        print("circle")
else:
    print("pass")

'''
Create a  that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
'''
def FizzBuzz(num):
    if num%3==0 :
        print("Fizz")
    elif num%3==0 & num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    else:
        print(str(num))

