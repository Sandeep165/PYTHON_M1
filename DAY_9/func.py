
def add(a,b,c):
    return(a+b+c)
    # print(a+b+c)

def greet(name):
    print(f"Good morning {name}!")

# greet("Anisha")
# greet("Aniket")
# greet("Shrenik")

# num +ve/-ve 
# def checkPositive(num):
#     if(num > 0):
#         print("Positive Number")
#     elif(num < 0):
#         print("Negative Number")
#     else:
#         print("Zero")

# checkPositive(7)
# checkPositive(-9)
# checkPositive(0)


# def checkPositive(num):
#     if (num > 0):
#          print("Positive Number")
#     elif (num==0):
#         print(" Number is Zero")
#     else:
#         print("Negative Number") 
# checkPositive(10)


#-1   1     -5  5    10.2    10
# def absoluteValue(num):
#     if num>=0:
#         print(int(num))
#     else:
#         print(-num)
# absoluteValue(-1)
# absoluteValue(10.2)
# absoluteValue(0)


num = 10 #global


# def display(num1):
#     num2 = 11 #local
#     print(num1)
#     print(num2)
#     print(num)

# display(11)
# print(num,num2)


# def greet(msg ,name):
#     print(f"Good morning {name}! from {msg}")

# greet("Prajakta")

#keyword argument    positional argument


def display(*names):
    for i in names:
        print(f"Good morning {i}")


# display("john","sam","tom")

def listelement(lst):
    for i in lst:
        print(i)

fruits = ["apple","mango","banana"]
listelement(fruits)

# def high(a,b,c):

def High(a,b,c):
    if(a>b and a>c):
        print("HIGHEST NUMBER:",a)
    elif (b>a and b>c):
        print("HIGHEST NUMBER:",b)
    else:
        print("HIGHEST NUMBER:",c)

# High(-10,-4,-7)




def high(a,b,c):
    if a>b & a>c:   # 1-1 bit
        print("A is the largest",a)
    elif b>a & b>c:
        print("B is the largest",b)
    else:
        print("C is the largest",c)

high(-1,7,-6)
'''
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals.
 The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species.
 You have to implement a function that returns the total number of legs of all the animals.
 (chickens,cows,pigs)

Examples
animals(2, 3, 5) ➞ 36

animals(1, 2, 3) ➞ 22

animals(5, 2, 8) ➞ 50
'''
# def animals(chickens,cows,pigs):
#     legs = chickens*2 + cows*4 + pigs*4
#     return legs
def animals(chick,cow,pig):
    if chick<0 & cow<0 & pig<0:
        print("invalid value")
    else:
        print(chick*2 + (cow+pig)*4)
animals(5,2,8)










