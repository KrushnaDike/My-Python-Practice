# def function1():
#     print("Krushna_Dike")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     elif num == 1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("This")
#
# executor(print)

#What is the Decorator ???

def dec1(func1):
    def nowexec():
        print("Executed Now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_krushna():
    print("Krushna is a Programmer")

# who_is_krushna = dec1(who_is_krushna)
who_is_krushna()