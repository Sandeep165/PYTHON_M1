'''
Create a class that imitates a select screen. For simplicity, the cursor can only move right!
In the display method, return a string representation of the list, but with square brackets around the currently selected element.
 Also, create the method to_the_right, which moves the cursor one element to the right.
The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"


Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually!
 As well as creating this Pizza class, hard-code the following pizza flavours.

Name	Ingredients
hawaiian	ham, pineapple
meat_festival	beef, meatball, bacon
garden_feast	spinach, olives, mushroom
Examples
p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]

p2.ingredients ➞ ["spinach", "olives", "mushroom"]

p1.order_number ➞ 1

p2.order_number ➞ 2

'''
class Pizza:
    # order_number = 1

    # def __init__(self,ingredients):
    #     self.ingredients = ingredients
    #     self.order_number= Pizza.order_number
    #     Pizza.order_number += 1
    order_number = 0

    def __init__(self,ingredients):
        self.ingredients = ingredients
        self.order_number= self.order()
 
    def order(self):
        Pizza.order_number += 1
        return Pizza.order_number
