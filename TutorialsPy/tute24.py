# try:
#     print("Enter num 1")
#     a = input()
#     print("Enter num 2")
#     b = input()
#     print("The sum of these two numbers is :",
#           int(a)+int(b))
# except Exception as e:
#     print(e)
#
# print("This is very important")
# print("#*#*#*#*#*#*#*#*#*#*#*#*#*# I'am Krushna dike #*#*#*#*#*#*#*#*#*#*#*#*#*#")

# Exception occurance
# print("Main area start")
# print(10/2)
# print(10/0)
# print("Main area end")

# print("Main area start")
# list1 = [10, 20, 30, 70]
# print(list1[0])
# print(list1[5])
# print("Main area end")

#try with multiple except block
# print("Main area start")
# try:
#     a = 10/2
#     print("Division is :",a)
#     print("Value of b is :",b)
# except ZeroDivisionError:
#     print("Exception occure:can not devided by zero")
# except NameError:
#     print("Exception occure:No such variable")
# print("Main area end")

# try:except:else block
# import os
# try:
#     os.rename("test1.txt","test01.txt")
#     print("Rename successfully.....!")
# except FileNotFoundError:
#     print("Exception occure:no such file or directory")
# else:
#     print("No Exception occure")

# except block with multiple exception
# import sys
# print("Main area start")
# i = 0
# while (i<=1):
#     try:
#         a = 10/i
#         print("Division is :",a)
#         print("Value of b is :",b)
#     except (ZeroDivisionError, NameError):
#         print("Exception occure:",sys.exc_info())
#     else:
#         print("No Exception occure")
#     i += 1
# print("Main area end")

# try:finally block
# print("Main area start")
# try:
#     f = open("test1.txt", "w")
#     f.write("This is line-1 in file")
#     f.write("This is line-2 in file")
#     print("Written Successfully...!")
# finally:
#     print("This statement must be execute")
#     print("Task done...!")
# print("Main area end")

# print("Main area start")
# try:
#     f = open("test1.txt","r")
#     print("File contains :\n",f.read())
# finally:
#     print("This statement must be excute")
#     print("Task done...!")
# print("Main area end")

"""we can see that in above two examples,
 finally block will be execute even exception occure or not"""

# try:except:finally block
# print("Main area start")
# try:
#     f = open("test1.txt","r")
#     print("File contains :\n",f.read())
# except FileNotFoundError:
#     print("Exception occure:No such file or directory")
# finally:
#     print("This statement must be excute")
#     print("Task done...!")
# print("Main area end")