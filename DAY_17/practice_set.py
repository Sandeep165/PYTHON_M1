'''
Q1:-  Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

Q3:- Write a Python program to compute the greatest common divisor (GCD) and LCD of two positive integers

Q4:-(edabit)
Write a function that returns the number of users in a chatroom based on the following rules:

If there is no one, return "no one online".
If there is 1 person, return "user1 online".
If there are 2 people, return user1 and user2 online".
If there are n>2 people, return the first two names and add "and n-2 more online".
For example, if there are 5 users, return:

"user1, user2 and 3 more online"

Example:- 
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"


Q5:-(edabit)
Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"


'''

# n = input().split()
# a=lambda n : n==list(set(n))
# print(a(n))
# def check(l):
#     # l = [1,2,3,4]
#     s = set(l)
#     if len(l) == len(s):
#         print(True)
#     else:
#         print(False) 
# l = [1,2,3,4,4]
# check(l)
# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
import random

# lst = ["a","e","i","o","u"]
for i in range(10):
    sample = ["a","b","c"]
    random.shuffle(sample)
    print(sample)


