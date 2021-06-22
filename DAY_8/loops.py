# while/for loop

# i = 1
# while i <= 20:
#     print(i)
#     i += 2  # i%2 == 0

i = 1

# while i <6:
#     print(i)
#     if i ==3:
#         break
#     i += 1

# while i <6:
#     print(i)
#     if i ==3:
#         pass
#     i += 1

# while i <6:
#     print(i)
#     if i == 3:
#         continue
#     i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         continue
#     print(i)
# #1 2 3 5 6

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# n = 10
# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i   # 0+1=1......#1+2 =3........
#     i += 1

# print("the sum of first 10 nums: ", sum)

# sum first 20 odd
# n=40
# m=1
# sum=0

# while m<=n:
#     sum+=m
#     m+=2
# print(sum)


# i = 1



# while i <6:
#     print(i)
#     if i == 3:
#         continue
#     i += 1


# i = 0
# while i < 6:
#     i += 1  #1
#     i += 1 #2
#     if i == 4:
#         continue
#     print(i)
# #2 6


# for loop

# for i in range(0,11):
#     print(i%2==0)

# list1 = ["apple","mango","banana"]
# for i in list1:
#     print(i) #appple mango.................
#     if i == "mango":
#         continue
#     print(i) #apple banana

# for i in range(10):
#     print(i)
# else:
#     print("Loop is over")
# list1 = ["apple","mango","banana"]
# list2 = [1,2,3]


# for j in list2:
#     print(j)
# # 1 , 2, 3

# for i in list1:
#     for j in list2:
#         print(j,i)

# sum of 10 evn ..... sum of 20 odd
# sum1=0
# sum2=0
# i=1
# for i in range(0,21,2):
#     sum1+=i
# print(sum1)
# i=1
# for i in range(1,41,2):  
#     sum2+=i
# print(sum2)
total = 0

# for i in range(1, 11):
#     if((i % 2) == 0):
#         total = total + i
# print(total)
# sum_even = 0
# sum_odd = 0
# count_even = 0
# for i in range(40):
#     if(i%2==0):
#         if(count_even <= 10):
#             sum_even += i
#             count_even +=1
#     else:
#         sum_odd +=i
# print(f"Sum of first 10 even numbers : {sum_even}")
# print(f"Sum of first 20 odd numbers : {sum_odd}")


list1 = [1,22,5,8,40,56]
sum = 0 

for i in list1:
    sum += i
print(sum)

# list2 = ["Shrenik","Anisha","Arya"]

# for i in list2:
#     print("Good Morning...", i)

# dict1 = {"Shrenik":75,"Anisha" : 95 , "Arya" : 70}
# name = input("Enter the name : ")

# for s in dict1:
#     if s == name:
#         print(dict1[s])
#         break
# else:
#     print("No data is found")

# # multiplication table 5
# for i in range(1,11):
#     print("5*",i,"=",5*i)

# x=5
# while(x<15):
#   print(x**2)
#   x+=3


b=15
while(b>9):
  print("Hello")
  b=b-2
