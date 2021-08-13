# Quize: Factorial of Number

# 1) By using For loop

# num = int(input("Enter Your Number :"))
# def factorial(n):
#     fac = 1
#     for i in range(1, n + 1):
#         fac = fac * i
#         yield fac
#
#     # return fac
# fact = factorial(num)
# print(fact)

"""
n! = n * (n-1) *........* 1
num = 5
5! = 5*4*3*2*1.. 
"""

# 2) By using While loop

# num = int(input("Enter a Number :"))
#
# def factorial(num):
#     fac = 1
#     i = 1
#     while i <= num:
#         fac = fac * i
#         i += 1
#
#     return fac
#
# fact = factorial(num)
# print(fact)

# Quize: Fibanacci series

# num = int(input("Enter a Number :"))
# def fibanacci(num):
#
#     for i in range(1, num+1):
#         if i == 1:
#             yield 0
#         elif i == 2:
#             yield 1
#         else:
#             yield fibanacci(num-1) + fibanacci(num-2)
#
# fib = fibanacci(num)
# print(fib)


def generator(num):
    for i in range(num):
        yield i

g = generator(4)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

str = "harry"
i = iter(str)
print(i.__next__())
print(i.__next__())

# for c in str:
#     print(c)
