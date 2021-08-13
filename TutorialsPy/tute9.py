stname = ["Krushna", "Mohini", "Bhagyashri", "Nikhil", 40, 55]
# print(type(stname))
# print(stname[5])

numbers = [2, 25, 8, 9, 93, 1, 63]
# print(type(numbers))
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(numbers[::-1])
# print(numbers[::])
# numbers.sort()
# numbers.reverse() # This two functions change the original list also
# print(numbers)

#Assignment Operator / updating list element by using (=)
# numbers[5]=10
# print(numbers)

#Adding element in list
# numbers.append(44)
# print("After appending list contains :",numbers)
#
# numbers.insert(1, 55)
# print("After Insertion operation list contains :",numbers)
#
# numbers2 = [15, 5, 2001, 32, 34, 57, 14]
# numbers.extend(numbers2)
# print("After extention numbers contains :",numbers)
# print("After extention numbers2 contains :",numbers2)

#Deleting element in list
    #keyword del
    #remove()
    #pop()
    #clear()

# del numbers[5]
# print("After deleting 5th index number :",numbers)

# del numbers
# print("After deleting whole list :",numbers) # it will show NameError

# numbers.remove(1)
# numbers.remove(93)
# print("After removing 1 and 93 item in list :",numbers)

# numbers.pop() #by default pop function remove last element of list
# print("After perform pop operation on list :",numbers)
# numbers.pop(0)
# print("After poping 0th index number :",numbers)

# Iterating through list by using while loop
# numbers3 =[93, 25, 63, 89, 59]
# print("Main area Start")
# i = 0
# while i<len(numbers3):
#     print("At index",i,"Element is",numbers3[i])
#     i += 1
# print("Main area end")

# #Iterating through list by using for loop
# numbers4 = [92, 84, 10, 32, 43]
# for item in numbers4:
#     print("Elements of list is :",item)

#Nested List
# list1 = ["krushna",[93, 25, 63, 89, 59], "Sanket", [92, 84, 10, 32, 43]]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
#we have nested list at index 1 and index 3
#now we can give the index number to nested list also
# print(list1[1][0]) #93 is identified as
# print(list1[3][2]) #10 is identified as

#example of append
# list2 = []
# print("Main area Start")
# print("Enter 5 elements to the list :")
# i = 0
# while i<=4:
#     ele = input()
#     list2.append(ele)
#     i += 1
# print("Elemetn of list2 contains :",list2)
# print("Main area End")


# mutable = can change
# Immutable = can not change

# tp = ()
# print(type(tp))
# print(tp)

# tp1 =(1, 2, 3)
# print(type(tp1))
# print(tp1)

# tp2 = (1) #single value se touple nahi banta esliye use single coma dena padta hai niche ke traha
# print(type(tp2))
# print(tp2)

# tp3 = (2,)
# print(type(tp3))
# print(tp3)

# tp4 = (4, "krushna", 55, [93, 25, 63, 89, 59], "Sanket") #mixed datatype
# print(type(tp4))
# print(tp4)
# tp4[0]= 44 #uski value change nahi hoti quiki touple immutable hain
# print(tp4)

# tp = ("krushna", 55, [93, 25, 63, 89, 59], "Sanket", [92, 84, 10, 32, 43])
# for item in tp:
#     print("Elements of Touple is :",item)

# print("Main area Start")
# i = 0
# while i<len(tp):
#     print("At index",i,"Element is",tp[i])
#     i += 1
# print("Main area end")