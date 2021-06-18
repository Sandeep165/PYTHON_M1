# range dict
# for i in range(0,10,1):
#     print(i)


# str1 = "Python and Javascript are the best"
# list1 = [1,2,3,4,5]

# for i in list1:
#     print(i)


# dict {}

'''
Unordered, Mutable,{}, key should be unique
'''


dict1 = { 1 : "Harry", 2 : "John", 3 : "Sam"}
print("\nDictionary with the integer keys: ")

my_dict = {
    "name" : "Curran",
    1 : [1,2,3,4]
}



print(my_dict)
print(type(dict1))
# dict1 = {
#     1 : "Harry", 
#     2 : "John", 
#     3 : "Sam"
# }

# my_dict1 = dict({1 : "apple", 2 : "grapes"})

# my_dict1 = dict([(1,"apple"), (2,"grapes")])
# print(my_dict1)

# print(type(my_dict1))


my_dict = {
    "name" : "Curran",
    "age"  : 21,
    1 : [1,2,3,4],
    False : "false",
    "tuple1" :  (1,2,3),
    "true" : ["mummbai","pune"]
}

#to retrive the values: 

# print(my_dict["name"])
# # print(my_dict[2])  #Keyerror
# print(my_dict.get(1)) 
# print(my_dict.get(2)) #None

# None ----> Nonedataype

#update the data

# my_dict["age"] = 31
# my_dict["country"] = "USA"
# print(my_dict)


square = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(square.pop(4))  # 16
# print(square.popitem())  # (5:25)
# print(square.clear())  
# del square
# print(square) 

new_dic = square 
# new_dic = square.copy()
print(new_dic.clear())  

# = assignment opertaor there will link(refrence)
# .copy()   another copy no link(refrence)

print(square)
print(new_dic)

#dict.formkey(key,value)

key = {"a","u" ,"i","o","e"}
val = {1,2,3,4,5}
vowels = dict.fromkeys(key,val)
print(vowels)


#key()  values()
square = {1:1, 2:4, 3:9, 4:16, 5:25}
print(square.keys())
print(square.values())


#update
a = {1 :"one", 2 :"two"}
# b = {2 :"three"}
b = {0 :"zero"}

a.update(b)
print(a)

