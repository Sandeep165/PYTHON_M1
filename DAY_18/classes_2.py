'''
Get the Area of a Country

completeformattingmathnumbersstrings
Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

Notes
The total world's landmass is 148,940,000 [Km^2]
Round the result to two decimal places.



'''


# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
# import random

# lst = ["a","e","i","o","u"]
# random.shuffle(lst)
# print(lst)

# res = "".join(lst)
# print(res)
# for i in range(10):
#     sample = ["a","b","c"]
#     random.shuffle(sample)
#     print(sample)
'''


Sort Positives, Keep Negatives
Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

Examples
pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

pos_neg_sort([]) ➞ []
Notes
If given an empty list, you should return an empty list.
Integers will always be either positive or negative (0 isn't included in the tests).
'''

# def remove_duplicates(value):
#     l1=[]
#     for i in value:
#         if i in l1:
#             l1.append(i)
#     return ''.join(l1)
# lst = ["1","2","2","3","4"]
# print(remove_duplicates(lst))

def fun1(lst):
    dup = []
    for i in lst:
        if (lst.count(i)>1) and (i not in dup):
            dup.append(i)
    return dup

lst = [1,2,3,4,4,5,6,6,4]
print(fun1(lst))