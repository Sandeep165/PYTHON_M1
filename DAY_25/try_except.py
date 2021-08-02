# try:
#     #code that we want to execute
#     #1. addition of two integer no.
#     #try execute successfully it will execute else block....Note : finally block is always excuted..
# except:
#     #exceptions that u want to handle
# else:

# finally:


# Example 1============================================================

# def divide(x,y):
#     try:
#         # floor division --give u fraction part of ur answer
#         #result = x//y 
#         result = x/y 
#         print("Your answer is :",result)
#     except:
#         print("Sorry u got an exception")
# divide(5,0)

# Example 2 ===================================================================
# def divide(x,y):
#     try:
#         # floor division --give u fraction part of ur answer
#         result = x//y         
#         print("Your answer is :",result)
#     #EXCEPTION TYPE
#     except ZeroDivisionError:
#         print("Zero division exception")

# divide(5,0)


# ====================================================
# with exception type and without exception type
# You can add many exception types with single problem
# Example 3 ==========================================

# def  abc(a,b):
#     try:
#         c=((a+b) /(a-b))
#     except ValueError:
#         print("Value are not in number")
#     except ZeroDivisionError:
#         print("Zero division")
#     else:
#         print(c)
#     finally:
#         print("I am always be there after completing...")

# abc(2.0,3.0)
# abc(3.0,3.0)


# Example 4 : Type Error (Datatype)
# def func(a):
#     try:
#         for i in range(a):
#             print(i)
#     except TypeError:
#         print("Type error")

# func(1.2)

#================================================
# Coversion operation of different datatype

# int(42) #already integer type  
# int("Sandeep")


# Example 5 : Diff between TypeError and ValueError ====================================
# import sys

# array_ex=['a',0,2]

# for i in array_ex:
#     try:
#         print("The array element : ",i)
#         res = 1/int(i)  # convert element into integer type
#     except ValueError:
#         print("Value Error")
#         print()
#     except ZeroDivisionError:
#         print("Zero Error")

# print("The reciprocal of ", i, "is", res)


#Example 6 : with sys library 

import sys

array_ex=['a',0,2]

for i in array_ex:
    try:
        print("The array element : ",i)
        res = 1/int(i)  # convert element into integer type
    except Exception as e:
        # print("Error :", sys.exc_info()[0])
        print("Error 2",e.__class__)

print("The reciprocal of ", i, "is", res)

