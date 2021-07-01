#decorator

# def inc(num):
#     return num - 2 

# def func2(func,num):
#     res =func(num)
#     return res

# print(func2(fun1,10))


# func1 ..... func2......op:- gd mrng students

#inc() +2... dec() -2.........oper(func,x)
# def inc(num):
#     return num + 2

# def dec(num):
#     return num-2

# def operator(func,num):
#     res = func(num)
#     return res

# print(operator(dec,15))
# print(operator(inc,15))


#1)sum 2)sub 3)choose
# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def operation(func,num1,num2):
#     res = func(num1, num2)
#     return res

# print(operation(add, 3, 5))
# print(operation(sub, 5, 9))

# def sum(a,b):
#     return a+b
# def diff(a,b):
#     return a-b
# def choose(func,a,b):
#     return func(a,b)
# print(choose(sum,1,2))
# print(choose(diff,1,2))


# def display():
#     print("Good afternoon...")
#     print("1")


# func = display
# # display()   #func call

# del display
# # display()  #
# func()     #

# def func(num):
#     if num == 0:
#         return print
#     if num ==1:
#         return sum
# res = func(0)
# print(res)
# res1 = func(1)
# print(res1)

# def show(print):
#     45.36==>45

# show(print)

#float = 45.65
#....(45)

# def f1(func,num):
#     return func(num)

# print(f1(int,45.65))

# def show(func):
#     res = func(45.36)
#     print(res)
# show(int)

# def show(func):
#     return func(45.65)
# print(show(int))

'''

def func1():
    print("msg")


def outer(func1):
    def inner():
        {logic1..}
        func1()
        {logic2...}
    return inner
    


'''
def outer(func):
    def inner():
        print(".........................")
        func()
        print(".........................")
    return inner


@outer   
def my_name():
    print("My self Coder!")

# my_name()
@outer
def add():
    print(5+4)
add()
