# a = 5
# b = 10
# c = sum((a, b)) #Built in Function
# print("Addition is :",c)

#User define Funcitons

# def function1():
#     print("Hello you are in function")
#
# function1()
# function1()
# function1()
# function1()


# def function2(a, b):
#     print("Addition is :",a+b)
#
# function2(10, 5)


def function3(a, b):
    """This is a function which will calculate average of two numbers
    This fuction doesnt work for three numbers"""
    average = (a+b)/2
    # print("Average is :",average)
    return average

# v = function3(10, 5)
# print(v)

print(function3.__doc__)

# function ke under pehli line pe comment out kiye huye line ko "docstring" kehte hain