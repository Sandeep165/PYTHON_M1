#Sequence Types:	list, tuple, range

#LIST----->mutable(change)

#empty list
my_list = []

# list of integer
my_list = [1,2,3,4]

#mixed data type list
my_list = [1,2,3,"pune",True,55]

#nested list

my_list1 = [1, 2, 3, 4, ["apple","mango"], 5]

# print(my_list1[0]) #1
# print(my_list1[2]) #3
# print(my_list1[4]) #['apple', 'mango'] {#apple, mango}
# print(my_list1[4][0])    #mango
# print(my_list1[5]) #5


my_countries = ["mumbai","pune",[400078,4000081,4000095,400051],["USA","JAPAN","AUS",["MEXICO"]],"NASHIK","DELHI"]
# 400095,Mexico,delhi 
# print(my_countries[2][2],",",my_countries[3][3][0],",",my_countries[5])
# print(my_countries[2][2], my_countries[3][3],my_countries[5])
# print(my_countries[2][2],my_countries[3][3][0],my_countries[5])




my_fruits = ["apple","mango",[[1,2,3,4],"hello_world"],"grapes"]
# 3, hello_world
# print(my_fruits[2][0][2],",",my_fruits[2][1])


list1 = [["harry","john"],1,4,6,9,["India"],400078]
# 9 , india, john
# print(list1[4],",",list1[5][0],",",list1[0][1])


# 400095,[Mexico],delhi
# 3, hello_world
# 9 , india, john

# print(my_countries[2][2], my_countries[3][-1][0], my_countries[-1])
# print(my_fruits[2][0][2], my_fruits[2][1])
# print(list1[4], list1[5][0], list1[0][-1])

#list() ----> list constructor

new_list = list(("apple","banana","mango"))
# print(new_list)


#Python Collection(Array)
'''
List ----> ordered data set, mutable, duplication are allowwed
Set
Tuple
Dict
'''

my_list = [1,2,3,"pune",True,55,1,2,3,"apple","banana","mango"]
my_list[3] = "mumbai"

#insert ------> append the value wherever u want
my_list.insert(3,4)  
my_list.insert(-1,"grapes") 
 

#append -----> end only
my_list.append("hello")

#extend
list_1 = [1,2,3]
list_2 = [4,5,6]
list_1.extend(list_2)
print(list_1)

fruits = ["apple","mango",1,2,3]
flowers = ("rose","sunflower")
fruits.extend(flowers)

#insert ------> append the value wherever u want
my_list.insert(3,4)  
my_list.insert(-1,"grapes") 

#remove
fruits.remove("sunflower")
print(fruits)


#append -----> end only
my_list.append("hello")

#pop 
fruits.pop(1)

for i in fruits:
    print(i)


#reverse  [::-1]
fruits.reverse()

#count
# print(fruits)
# print(fruits.count("apple"))


'''
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()  	Sorts the list

'''

string = ["apple","applae","mango","grapes"]
string.sort()
# print(string)

integer =  [5,6,87,2,1,6,3] 
integer.sort(reverse=True)
print(integer)



