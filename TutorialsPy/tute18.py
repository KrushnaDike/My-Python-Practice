# keyword 'break'
# i = 0
# while (True):
#     print(i, end=" ")
#     if i>=45:
#         break #stop the loop
#     i += 1

#keyword 'continue'
# i = 0
# while (True):
#     if i<=5:
#         i += 1
#         continue
#
#     print(i, end=" ")
#     if i>=45:
#         break #stop the loop
#     i += 1

#Quize

while (True):
    num = int(input("Enter a number :\n"))
    if num<100:
        print("Try again..!\n")
        continue

    else:
        print("Congrats bro..!You enter greater that 100 number\n")
        break
