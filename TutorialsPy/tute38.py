# import random
import datetime
import math
import calendar
#
# random_integer = random.randint(0, 10)
# print("Random iteger between 0 to 10 :\n",random_integer)
#
# random_number = random.random() * 100
# print("Random number between 0 to 100 :\n",random_number)
#
# list1 = ["Krushna","Sanket","Nikhil","Kumar","Amit"]
# random_choice = random.choice(list1)
# print("Random choice between the list :\n",random_choice)



# from PIL import Image
#
# img  = Image.open("Veer_Shivaji.img.jpg").convert("L")
# print(img.format)
# print(img.mode)
# print(img.size)
# img.resize((40, 60)).show()
# img.rotate(45).show()
# # img.show()
# img.save("Veer_Shivaji_gs.jpg")



import time
# a = time.gmtime()

# a = time.localtime()
# print(a.tm_year)
# print(a.tm_hour)

# a = time.asctime()
# a = time.time()
# print(a)

# print("This is printed")
# time.sleep(2.5)
# print("This is printed after 2.5 secs")

# time_string = time.strftime("%m/%d/%Y, %H:%M:%S")
# print(time_string)

# print(a)



# fac = math.factorial(8)
# print(fac)
#
# sqrt = math.sqrt(25)
# print(sqrt)



# calendar = calendar.calendar(2020, 2)
# print(calendar)



# from datetime import date
# today = date.today()
# print(today)



# import platform
# plat = platform.system()
# print(plat)


import os

# getcwd()
# print(f"The current working directory is : {os.getcwd()}")

# chdir()
# print(f"Before changing derectory : {os.getcwd()}")
# os.chdir("D:\\")
# print(f"after changing derectory : {os.getcwd()}")

# listdir()
# print(f"The current working directory is : {os.getcwd()}")
# print(f"This derectory contains : {os.listdir()}")

# mkdir()
# print(f"The current working directory is : {os.getcwd()}")
# print(f"Before creating new directory : {os.listdir()}")
# os.mkdir("new_dir.py")
# print(f"After creating new directory : {os.listdir()}")

# rename()
# print(f"The current working directory is : {os.getcwd()}")
# print(f"Before creating new directory : {os.listdir()}")
# os.mkdir("new_dir.py")
# print(f"After creating new directory : {os.listdir()}")
# os.rename("new_dir.py", "new_dir1")
# print(f"After renaming these new created directory : {os.listdir()}")

# path.exists()
# print("This c:\\Program Files is exits :", os.path.exists("c:\\Program Files"))
# print("This c:\\Program Files1 is exits :", os.path.exists("c:\\Program Files1"))

# path.isdir()
# print("This c:\\Program Files is a directory :", os.path.isdir("c:\\Program Files"))
# print("This c:\\Program Files1 is a directory :", os.path.exists("c:\\Program Files1"))