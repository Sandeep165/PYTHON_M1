'''
Q1:- 
Given a list of numbers, write a Python program to count Even and Odd numbers in a List.
Using lambda

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2


Q2:- 
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the
duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.



Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. 
Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])
menu.display() ➞ [[1], 2, 3]
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"



Create a function that performs an even-odd transform to a list, n times. Each even-odd transformation:

Adds two (+2) to each odd integer.
Subtracts two (-2) from each even integer.
Examples
even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
# Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]

even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]


'''

def even_odd(lst,n):
    op_lst = []
    for i in lst:
        if i%2 == 0:
            op_lst.append(i-2*n)
        else:
            op_lst.append(i+2*n)

    return op_lst


def even_odd_transform(l1, n):

    for j in range(n):
        for i in range(0, len(l1)):
            if l1[i] % 2 != 0:
                l1[i] = l1[i] + 2
            else:
                l1[i] = l1[i] - 2

    return l1


print(even_odd_transform([3, 4, 9], 3))
print(even_odd_transform([0, 0, 0], 10))
