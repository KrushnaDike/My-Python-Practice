# var1 = 5
# var2 = 50
# var3 = int(input("Enter a number :"))
#
# if var3>var2:
#     print("Greater..!")
# elif var3==var2:
#     print("Ha ha h..Equal..!")
# else:
#     print("Lesser..!")

# list1 = [50, 93, 25, 92, 63, 89, 59]
# # print(51 in list1)
# i = int(input())
# if i in list1:
#     print("Yes, it's in list")
# elif i not in list1:
#     print("No, it's not in list")
# else:
#     print("Error..!")

#Quize
age = int(input("Enter your age :"))
if age>18:
    if age<100:
        print("You can drive the car")
    else:
        print("Error..!Check your Input")
elif age<18:
    if age>7:
        print("You can not drive the car")
    else:
        print("Error..!Check your Input")
elif age==18:
    print("I will discus about you")

#Nested if statement

# n1 = int(input("Enter First No :"))
# n2 = int(input("Enter Second No :"))
# n3 = int(input("Enter Third No :"))
#
# if n1>n2:
#     if n1>n3:
#         print("n1 is Greater..!")
#
# if n2>n1:
#     if n2>n3:
#         print("n2 is Greater..!")
#
# if n3>n1:
#     if n3>n2:
#         print("n3 is Greater..!")