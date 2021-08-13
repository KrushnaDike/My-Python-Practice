# Pattern Printing

# By using while loop

# n = int(input("Enter a Number :"))
# bool2 = int(input("Enter 1 for TRUE and 0 for FALSE :"))
# bool(bool2)
# if bool2 == False:
#     i = 0
#     while n>=i:
#         print("*"*n)
#         n -= 1
# elif bool2 == True:
#     i = 0
#     while i<=n:
#         print("*"*i)
#         i += 1
# else:
#     print("Plz Enter Correct Input...!")

# By using for loop

n = int(input("Enter a Number :"))
bool2 = int(input("Enter 1 for TRUE and 0 for FALSE :"))
bool(bool2)

if bool2 == True:
    for i in range(0, n+1):
        print("❤"*i)
elif bool2 == False:
    for i in range(n, 0, -1):
        print("❤"*i)
