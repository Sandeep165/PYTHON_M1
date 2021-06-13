'''
python functional as well as object oriented prog lang
python are totaly based on objects and classes


# var name has to be start with alpha numeric
# it should not start  with spcl char and keyword
# cannot start with numbers
# var can stat with _(underscore) 

true = "Harry"
list = 15 # wrong
my_var = "Hello"
_myvar = "Hello"
my_var = "Hello"

5myvar = "hello" #bcz start int
my-var = "harry" #- is not expected
my var =  "hie"  # spaces are not allowed

age = 15
AGE = 15
'''


# num = 12 #int
# str1 = "hello"
# str2 = 'hello'
# str3 = ''' hello my name is harry '''

# print(type(str1))

# num = int(input("Enter the number 1 :"))
# print("User entered the number ", num)

x, y, z = "apple", "mango", "orange"
x, y, z = 'apple', 'orange', 'mango'
# print(x, y, z, sep='\n')

# print(x)
# print(y)
# print(z)


'''
string formatting ?

fname = "Sandeep"
age = 21
city = "mumbai"
hobby = "cricket"

print("My first name is ", fname, "my age is ", age) #method 1

print("My name is {}. my age is {}".format("Sandeep",21)) #string formatting  method 2

print(f"My name is {fname}. my age is {age} i stay in {city} love to play {hobby}")  #method 3
'''
# num = int(input("enter the number: "))
# name = input("enetr your name")

# x = str(3)
# x = int(3)   # x = 3
# name = "john"
# name = 'john'
# name = '''john'''

# print(type(x))


'''
my poem is:
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
'''
# print("my poem is:\nTwinkle, twinkle, little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky\nTwinkle, twinkle, little star\nHow I wonder what you are")
# print("My Poem is :", "Twinkle, twinkle, little star", "How I wonder what you are", "Up above the world so high", "Like a diamond in the sky", "Twinkle, twinkle, little star", "How I wonder what you are", sep="\n")


# print('''
# my poem is:
# Twinkle, twinkle, little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle, twinkle, little star
# How I wonder what you are
# ''')


# comments pip
# inbuild install manually
# REPL read eval print loop  exit()


'''
types of data types in python(category):-

Text Type:	str
Numeric Types:	int, float, complex(ai+bj)
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool(true/false)
# Binary Types:	bytes, bytearray, memoryview

'''

# list
list1 = [1, 2, 3, 4]
print(list1)
print(type(list1))
x = 5
x = int(5)
num = list(list1)


# set
set1 = {"apple", "mango"}
print(set1)
print(type(set1))
country = ["India", "NZ", "Japan"]
country = set(country)  # set constructor
print(type(country))  # class<set>


# tuple
tuple1 = ("apple ", "mangp", "10")
print(tuple1)
print(type(tuple1))

#Dict
dict1 = {"name" : "harry", "age" : 15  }
print(dict1)
print(type(dict1))


# range()
print(1)
print(2)
print(3)
x = range(10)
print(x)
print(type(x))

for i in range(0,11,2):
    print(i)

    #0 - 10
    #1 - 10

#range(10)      #stop..........exclusive
#range(1,10)    #start(inclusive) stop
#range(1,10,1)  #start stop step

#frozenset: takes input as an iterable object and convert them into an immutable object
x = frozenset({"apple","mango","cherry"})
print(x)
print(type(x))


#bool
x = True 

print(x)
print(type(x))


#byte bytearray memoryview

x = b"Harry"
print(x)
print(type(x))
arr = "I love python"

str1 = bytes(arr, 'utf8')
print(str1)


y = bytearray(5)
print(y)
print(type(y))

size = 5
arr = bytearray(size)
print(arr)


val1 = memoryview(bytes(5))
print(val1)
