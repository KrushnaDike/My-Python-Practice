# # def add(a, b):
# #     return a+b
#
# add = lambda a,b: a+b
# print(add(5, 5))
#
# # def sub(x, y):
# #     return x-y
#
# sub = lambda x, y: x-y
# print(sub(10, 5))



# def a_first(a):
#     return a[2]

a_first = lambda a : a[2]
a = [[10, 50, 100], [5, 60, 10], [1, 100, 40]]
a.sort(key=a_first)
print(a)