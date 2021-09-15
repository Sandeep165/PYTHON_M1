'''
Create a function (named fifth) that takes some arguments and returns the type of the fifth argument.
 In case the arguments were less than 5, return "Not enough arguments".

Examples
fifth(1, 2, 3, 4, 5) ➞ int

fifth("a", 2, 3, [1, 2, 3], "five") ➞ str

fifth() ➞ "Not enough arguments"





Create methods for the Calculator class that can do the following:
•	Add two numbers.
•	Subtract two numbers.
•	Multiply two numbers.
•	Divide two numbers.
Examples
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2
Notes
•	The methods should return the result of the calculation.
•	Don't worry about needing to handle division by zero errors.
•	See the Resources tab for some helpful tutorials on Python classes.
   




Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as 
input.
You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually! As
well as creating this Pizza class, hard-code the following pizza flavours.

Name        	     Ingredients
hawaiian    	     ham, pineapple
meat_festival	     beef, meatball, bacon
garden_feast	     spinach, olives, mushroom

Examples
p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]
p2.ingredients ➞ ["spinach", "olives", "mushroom"]
p1.order_number ➞ 1
p2.order_number ➞ 2
Notes
All words are given in lowercase.




Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
The flowers are identified using name, price per kg and stock available (in kgs).
Write a Python program to implement the above requirement.
Details of Flower class are given below:

Class name: Flower
Attributes
(private)	:-
                flower_name
                price_per_kg
                stock_available	 
Methods
(public)	         __init__():- 	Create and initialize all instance variables to None
	                 validate_flower():- 	Return true, if flower name is valid. Else, return false
                (Refer table for valid flower names)
	                validate_stock(required_quantity):- 	Accept the quantity required. Return true, if stock is available.
                Else return false.
	                sell_flower(required_quantity):- 	Accept the quantity required.
                Validate flower name and stock.
                If both are valid, update stock available based on the quantity required
	                check_level():- 	Check if available stock is below the order level
                If so, return true. Else, return false
                (Refer table for order level of each flower)
	                setter methods:-	Include setter methods for all instance variables to set its values
	                getter methods:-	Include getter methods for all instance variables to get its values
 
 
Flower Name	        Level(in Kgs)
Orchid              	15
Rose	                25
Jasmine             	40


Note: Perform case insensitive string comparison
Represent few flowers, initialize instance variables using setter methods, invoke appropriate methods and test your program.



'''