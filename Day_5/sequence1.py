#tuple ---> ()
'''
Tuple is immutable
Tuple is ordered data set
Duplications are allowed
Tuple capable of holding diffrent data types
'''


# print(my_tuple)
# print(type(my_tuple))

#tuple() constructor

# myTuple = tuple(my_tuple)
# print(len(my_tuple))
# print(my_tuple[len(my_tuple)-1])

# my_tuple = my_tuple[:4] + ('Pune',) + my_tuple[5:]
# a = list(my_tuple)
# a[4] = "Pune"
# my_tuple = tuple(a)
# print(my_tuple)
# print(my_tuple.append("delhi"))
my_tuple = (1,2,3,4,"Mumbai",True,1.5)

# del my_tuple
# print(my_tuple)


#unpacking

fruits = ("apple","mango","grapes",1,2,3,4) #packing

(a,*b,c) = fruits  #unpacking     a b c = apple mango grapes
# print(a, b, c)


# tuple1 = ("Mumbai","Pune",1,2,3,4,1.5,True, [1,2,3])
# print(len(tuple1))
# print(tuple1[8][1])

# print(tuple1[-1][1])

# for i in tuple1:
#     print(i)

tuple1 = ("Mumbai","Pune",1,2,3,4,1.5, [1,2,3])
tuple2 = (True,False)


tuple3 = tuple1 + tuple2 
print(tuple3)

#tuple method
#count   
#index 

print(tuple1.count(1)) 

print(tuple1.index(1.5))
