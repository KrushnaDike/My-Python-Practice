# List Comprehention

# lst = []
#
# for i in range(100):
#     if i%3 == 0:
#         lst.append(i)

# lst = [i for i in range(100) if i%3==0]
#
# print(lst)

# Dictionary Comprehention

# dict = {0:"Item0", 1:"Item1",.......}
#
# dict = {i:f"Item{i}" for i in range(1,10001) if i%100==0}
# dict = {i:f"Item{i}" for i in range(5)}
# dict1 = {value:key for key,value in dict.items()}
#
# print(dict ,"\n", dict1)

# Set Comprehention

# dresses = {dress for dress in ["dress1", "dress2","dress1", "dress2","dress1", "dress2","dress1", "dress2"]}
#
# print(dresses)

# Generator Comprehention

# evens = (i for i in range(100) if i%2==0)
# # print(evens.__next__())
# # print(evens.__next__())
# 
# for i in evens:
#     print(i)

# Quize:

lst = []
n = int(input("How many items you want to add :"))
i = 1
while i <= n:
    item = int(input(f"Enter your list Item (only integer){i}:"))
    lst.append(item)
    i += 1
    
print("1) List Comprehension\n"
      "2) Dictionary Comprehension\n"
      "3) Set Comprehension\n"
      "4) Exit.")
com = int(input("Which type of comprehension you want to create :"))

if com == 1:
    lst2 = [i for i in lst if i%8==0]
    print("List Comprehension is :",lst2)

elif com == 2:
    dict1 = {index:f"Iitem{value}" for index,value in enumerate(lst) if value>=70}
    print("Dict Comprehension is :",dict1)

elif com == 3:
    set = {i for i in lst if i%2==0}
    print("Set Comprehension is :",set)

elif com == 4:
    print("Thanks for using my software...!")
    exit()

else:
    print("Invalid Input")