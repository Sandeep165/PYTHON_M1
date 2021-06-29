nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# square = list(filter(lambda x : x**2,nums))
# print(f"original list before map is: {nums} and after map it will: {square}")


# # even = list(map(lambda x: x%2 ==0 ,nums))
# # print(f"original list : {nums} and after map it becomes: {even}")


# # map....func().....obj in the iterable
# # filter....func()....for which value ur func returns true:

# iterator....genrator
# iterator.....iter()......next()

# mytuple = ('apple',"mango","banana","grapes")
# # for i in mytuple:
#     # print(i)

# myIter = iter(mytuple)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(myIter.__next__())
# print(next(myIter))


# genrator

# def my_gen():
#     n = 1
#     print("This is printed first")
#     yield n

#     n += 1
#     print("this is printed second")
#     yield n

#     n += 1
#     print("At last")
#     yield n


# # a = my_gen()
# for i in my_gen():
#     print(i)


# next(a)
# next(a)
# next(a)
# next(a)


# OOPS----->Object oriented prog
# DRY---->function/oops====DO NOT REPEAT YOURELF

'''

def xyz():------> fun def
    body{}   --> fun body
xyz()----------> fun call



#self
class xyz:
    {cls_body...methods}

obj1 = xyz()

 
'''
# name = input("name :")


class Birds:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name of the bird is {self.name} age is {self.age}")

# whatever number of parameter you are passing inside the constructor the same no of argu you need to pass in obj creation
# obj1 = Birds("Parrot",5)      #birds.__init__()
# print(obj1.name)
# obj1.display()


# class cal.....add subs mul....const(num1,num2)
class Cal:
    species = "Flying.."  # class varibale

    def __init__(self, num1, num2):
        self.num1 = num1  # instance varibale
        self.num2 = num2
        print("inside the constructor")

    def add(self):
        print("Addition of ", self.num1, " and ",
              self.num2, "is ", self.num1+self.num2)

    def sub(self):
        print("Subtraction of ", self.num1, " and ",
              self.num2, "is ", self.num1-self.num2)

    def mul(self):
        print("Multiplication of ", self.num1, " and ",
              self.num2, "is ", self.num1*self.num2)


obj1 = Cal(10, 5)
# obj1.add()
# obj1.sub()
# obj1.mul()
