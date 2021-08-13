s = set()
# print(type(s))

#We can declare the set by using following two methods refer (s1, s2)
s1 = {10, 92, 20, 59, 30, 40, 89}
l = [10,20, 25, 30, 63,  40, 93]
s2 = set(l)
# print("s1 contains :",s1)
# print("s2 contains :",s2)
# print("type of s1 :",type(s1))
# print("type of s2 :",type(s2))

"""
Dont confuse with carly braces, if we use key:value pairs inside the curly 
braces the it will creates dectionary, but if we use only elements inside 
the curly braces the it will creates ste. One more thing empty croly braces 
also denotes the dectionary.
"""
# s3 = {}
# print(type(s3))
# s4 = {1, 2, 3, 4}
# print(type(s4))

#Accesing set element by using for loop
# for item in s1:
#     print("Element of set is :", item)

# for item in s1:
#     sq = item * item
#     cu = item * item *item
#     print("square is :",sq)
#     print("cube is :",cu)

#Adding element in set by using add() and update()
# s1.add(44)
# s1.add(44)
# s1.update([93, 25, 63, 89, 59],{92, 8401, 3243})
# print(s1)

#Deleting element from set
    #keyword 'del'
    #remove()
    #pop()
    #clear()
    #discard()

# del s1
# print(s1)

# s1.remove(93)
# print(s1)

# print("Before pop operation :",s1)
# s1.pop()
# s1.pop()
# s1.pop()
# s1.pop()
# print("After pop operation :",s1)

# s1.clear()
# print(s1)

# s1.discard(63)
# s1.discard(20)
# print(s1)

# print(s1.isdisjoint(s2))

#Intersection
s5 = s1.intersection(s2)
# s5 = s1&s2
print("Intersection of s1 and s2 :",s5)

# Symentric Difference
s5 = s1.symmetric_difference(s2)
print("symentric_diffence is :", s5)

# Difference
s5 = s1.difference(s2)
print("Difference of s1 is :",s5)
s6 = s2.difference(s1)
print("Difference of s2 is :",s6)
