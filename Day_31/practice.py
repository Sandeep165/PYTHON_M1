'''

Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be 
accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"

'''

class User:
    count = 0
    def __init__(self,u_name):
        self.uname = u_name
        User.count += 1


'''

Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest icecream. 
Note that there is a class is provided for you in the Tests tab.

class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles
Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.

Flavors 	Sweetness Value
Plain	        0
Vanilla     	5
ChocolateChip	5
Strawberry     	10
Chocolate	    10

Examples
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23

sweetest_icecream([ice3, ice1]) ➞ 23

sweetest_icecream([ice3, ice5]) ➞ 17

Write a Python program to find intersection of two given arrays using Lambda. Go to the editor
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]

'''

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
results = list(filter(lambda i: i  in l1,l2))
print(results)