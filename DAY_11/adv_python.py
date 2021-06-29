# '''

# def xyz():------------> func def(parameter)
#     logic1
#     logic2--------------> func body

# xyz()------------------>func call(arguments)

# '''
# '''num1 = 10
# num2 = 1
# num3 = 3
# print(num1 >num2 & num1>num3)
# print(4&5)'''
# # binary addition
# '''
# def high(a,b,c):
#     if a>b and a>c:
#         print(c,' is the highest')
#     elif b>a and b>c:
#         print(b, ' is the highest')
#     else:
#         print(a, ' is the highest')
# high(-11,2,0)
# # cond1 and cond2 ------> true/ false
# # True & False-------->  true/ false
# num1 = 6
# num2 = 5
# num3 = 4
# print(num1 >num2 and num1>num3)  #True
# # print(num1 >num2 & num1>num3)    #False
# print(4&5) #4
# print(9&1)  #1001 & 0001-----> 0001(1)
# {421}
# 1    001
# 2    010
# 3    011
# 4    100
# 5    101
# 6    110
# 100 (4)
# 101 (5)
# ---
# 100 (4)
# '''

# # lst = [0.......11]
# # 2 4 6 8
# def even(num):
#     for i in num:
#         if i%2 != 0:
#             print(i)
# lst = [0,1,2,3,4,5,6,7,8,9,10,11]
# # even(lst)


# def odd(*num):
#     for i in num:
#         print(i)
#     print("the count is: ",len(num))
#     print(type(num))

# # odd(1,2,3,4,5,6,9,1,2,5,4,8,9,3,5)


# # Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# # and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater
# # than 7, the function should return None.

# # Expected output
# # returnDay(1) --> Sunday


# # Write a function called lastElement. This function takes one parameter (a list)
# # and returns the last value in the list. It should return None if the list is empty.

# # Example Output
# # lastElement([1,2,3]) # 3
# def lastElement(lst):
#     print(lst)
# # lst = [1,2,4,5,6]
# # lastElement(lst)


# # fun   sum(num) -------(8,2,7,9)
# def sum(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     print(f"Sum = {sum}")

# # sum(8,2,7,9)


# # def even(data):
# #     e = []
# #     # if i %2 == 0:
# #     e.append(i)
# #     print(e)

# # even([1,2,3,4,5,6,7,8,9,10,12,14,19])
# # e = [2,4,6,8,10,12,14]

# # def even_odd(data):
# #     e = []
# #     for i in data:
# #         if i % 2 == 0 :
# #             e.append(i)
# #     print(e)
# #     o = []
# #     for j in data:
# #         if j%2 != 0:
# #             o.append(j)
# #     print(o)


# # even([1,2,3,4,5,6,7,8,9,10,12,14,19])

# # in / not in

# strong1 = "love"
# strong2 = "love python"

# print(strong2 in strong1)


# #list = [1,2,3,4,5,6,1,3,6]
# #uni_lst = [1,2,3,4,5,6]

# def unique(lst):
#     lst1 = []
#     for i in lst:
#         if i not in lst1:
#             lst1.append(i)
#     return lst1

# print(unique([1,2,3,4,5,6,1,2,3]))


# def uni_lst(lst):
#     unique = set(lst)
#     unique = list(unique)
#     print(unique)

# uni_lst([1,2,2,2,3,4,6,5,3,4,1,9])


# Why is list index out of range
# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(len(number_list)) #10
# for i in range(len(number_list)):
#     if number_list[i]>50:
#         # del number_list[i]
#         print(number_list[i])
# print(number_list)
'''

returnDay.
# This function takes in one parameter ( a number from 1-7)
# and returns the day of the week
# ( 1 is Sunday, 2 is Monday etc.).
# If the number is less than 1 or greater
# than 7, the function should return "None".


'''

# def returnDay(num):
#     dict1={}
#     list1=['sun','mon','tue','wed','thu','fri','sat']
#     for i in range(1,8):
#         dict1[i]=list1[i-1]
#     print(dict1.get(num))

# returnDay(4)
# def returnDay(value):
#     dict1 = {1 : "Sunday",
#              2 : "Monday",
#              3 : "Tuesday",
#              4 : "Wednesday",
#              5 : "Thursday",
#              6 : "Friday",
#              7 : "Saturday"}
#     if value >0 and value <=7:
#         print(dict1[value])
#     else:
#         print(None)
# returnDay(0)
# def returnDay(iDay):
#     myDayDict = {1 : 'Sunday', 2: 'Monday', 3:'Wednesday', 4 : 'Thrusday', 5:'Friday',
#                 6:'Saturday', 7:'Sunday'}
#     return myDayDict.get(iDay, None)

# print(returnDay(50))

# def f():
#     global a
#     print(a)
#     a = "Hello"
#     print(a)

# a = "world"
# f()
# print(a)


# x = 5
# def f1():
#     global x
#     x = 4


# def f2(a,b):
#     global x
#     return a+b+x


# f1()
# total = f2(1,2)
# print(total)


# x = 10
# def f(x):
#     x =5
#     print(x)
#     x=15

# f(x)    #5
# print(x)#15, 10


# lambda fun

# lambda args:expression

# 5,,,,,,10     8....16

# def double(x):
#     return x*2

# print(double(10))

res = lambda *nums: print(nums)
res(10, 12, 15, 22)

# fliter n map.....
list1 = [1,2,5,0,10,8,80,90,14,1,5,6,7,15,41]
def even(lst):
    e = []
    for i in lst:
        i%2 == 0
        e.append(i)
    print(e)

even = list(filter(lambda x: (x%2 ==0), list1 ))
# print(even)


list1 = [1,2,5,0,10,8,80,90,14,1,5,6,7,15,41]
# list2=list(filter(lambda x: x>10,list1))
# print(list2)
list2 = list(map(lambda x: x*2, list1))
print(list2)