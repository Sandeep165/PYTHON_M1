'''


Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. 
A grocery dictionary has a product, a quantity and a price, for example:

{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
Examples
# 1 bottle of milk:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]) ➞ 1.5

# 1 bottle of milk & 1 box of cereals:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]) ➞ 4

# 3 bottles of milk:
get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]) ➞ 4.5

# Several groceries:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]) ➞ 10.4

# Some cheap candy:
get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
]) ➞ 0.3



'''
def get_total_prize(groceries):
    sum=0
    for i in groceries:
        sum+=i['quantity']*i['price']
    return round(sum,1)


def get_total_price(groceries):
    total=0.0
    for i in groceries:
        quantity=i.get("quantity")
        price=i.get("price")
        total+=float(quantity)*float(price)
    print(total)


'''

Create a class with a couple of functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters with another characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string that truncates spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are among the specified indexes.
If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"


'''

class magic:

    def replace(self,str1,b,c):
        return str1.replace(b,c) 

    def str_length(self,str1):
        return len(str1)

    def trim(self,str1):
        return str1.strip()
        
print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("      python is awesome      "))


class Magic:

    def replace(self,str1,b,c):
        return str1.replace(b,c) 

    def str_length(self,str1):
        return len(str1)

    def trim(self,str1):
        return str1.strip()
magic=Magic()
print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("   python is awesome      "))

'''
This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:

First character of next word must match last character of previous word.
The word must not have already been said.
Below is an example of a Shiritori game:

["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!

["motive", "beach"]  # invalid! - beach should start with "e"

["hive", "eh", "hive"]  # invalid! - "hive" has already been said
Write a Shiritori class that has two instance variables:

words: a list of words already said.
game_over: a boolean that is true if the game is over.
and two instance methods:

play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).

If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

Examples
my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart() ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.

'''
class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

class Shiritori:

    def __init__(self,words = [] ,game_over=False):
        self.words = words
        self.game_over = game_over
    
    def play(self):
        pass

    def restart(self):
        self.words = []
        self.game_over = False
        return("game restarted")
