# def print2(str):
#     print2(str)
#     print("This is " + str)
# print2("Krushna")



# # n! = n * (n-1) * (n-2) * (n-3)......1
# # n! = n * (n-1)!
# def factorial_iterative(n):
#     """
#
#     :param n: Integer
#     :return: n * (n-1) * (n-2) * (n-3)......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#
# # 5 * factorial_recursive(4)
# # 5 * 4 * factorial_recursive(3)
# # 5 * 4 * 3 * factorial_recursive(2)
# # 5 * 4 * 3 * 2 * 1
#
# number = int(input("Enter a number :"))
# # factorial_iterative(number)
# print("Factorial using iterative method :",factorial_iterative(number))
# print("Factorial using recursive method :",factorial_recursive(number))

# 0 1 1 2 3 5 8 13
def fibanacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibanacci(n-1)+fibanacci(n-2)

number = int(input("Enter a number :"))
print(fibanacci(number))