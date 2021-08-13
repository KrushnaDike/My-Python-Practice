# i = -1
# while i<1:
#     i += 1
#     try:
#         div = 10/i
#         print(div)
#
#
#     except Exception as e:
#         print(e)
#
#     finally:
#         print("This block is run by when exception occure or not, this will not care..!")
#
#     print("Important stuff..!")
#
# else:
#     print("This block is run by when exception is not occure.")
#

f1 = open("krushna.txt")
try:
    f = open("does.txt")

except Exception as e:
    print(e)

else:
    print("This block is run when exception is not occure.")

finally:
    print("Run this anyway...")
    f1.close()
    try:
        f.close()
    except Exception as e:
        print("File is not exists.")

print("Important stuff..!")


