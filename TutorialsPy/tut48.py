# =================================== map() ===============================
lst = ["2", "20", "40"]
# print(lst)
# print(map(int, lst))
# lst = list(map(int, lst))

# for i in range(len(lst)):
#     lst[i] = int(lst[i])

# lst[2] = lst[2] + 1
# print(lst[2])


# def sq(num):
#     return num * num
#
# lst1 = [2, 45, 85, 7, 9, 4]
# square = list(map(sq, lst1))
# print(square)

# sq = lambda num: num*num
# lst1 = [2, 45, 85, 7, 9, 4]
# square = list(map(sq, lst1))
# print(square)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# lst2 = [square, cube]

# def func(x):
#     return x(i)
#
# for i in range(5):
#     lst3 = list(map(func, lst2))
#     print(lst3)

# for i in range(50):
#     lst3 = list(map(lambda x:x(i), lst2))
#     print(lst3)


# =========================== filter() =============================
# list1 = [2, 4, 100, 3, 5, 6, 10, 14, 80]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)

# ============================== reduce() =============================
from functools import reduce
list1 = [1, 2, 3, 4, 7,40]
# def add(x, y):
#     return x+y
num = reduce(lambda x, y: x+y, list1)
print(num)

# num = 0
# for item in list1:
#     num = num + item
#
# print(num)