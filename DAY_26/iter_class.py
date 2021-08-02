# list1 = [1,2,3,4,5]
# # myIter = list1.__iter__()
# myIter = iter(list1)

# while(True):
#     try:
#         print(next(myIter))  
#     except StopIteration:
#         break


# class Iter_2:
#     def __iter__(self):
#         self.num = 0
#         return self
    
#     def __next__(self):
#         num = self.num
#         self.num += 2
#         return num

# obj1 = iter(Iter_2())

# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))

# class Even:
#     def __init__(self,max_num):
#         self.n = 2
#         self.max_num = max_num

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n <= self.max_num:
#             result = self.n
#             self.n += 2
#             return result
#         else:
#             raise StopIteration

# obj1 = Even(14)
# # print(next(obj1))
# # print(next(obj1))
# # print(next(obj1))
# # print(next(obj1))
# # print(next(obj1))
# # print(next(obj1))
# # for i in Even(20):
# #     print(i)
# for i in obj1:
    # print(i)


class Pow_2:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n<= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

nums = Pow_2(3)
i = iter(nums)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
