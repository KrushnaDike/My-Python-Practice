# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book in code with harry and harry is good boy"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Your text is not in the book")
#
# search = searcher()
# search.__next__()
# # next(search)
# i = 0
# while i<5:
#     s = input("Enter what you want to search :")
#     search.send(s)
#     i += 1
#
# search.close()

def search_name():
    import time
    name_lst = ["krushna", "sanket", "Nikhil", "bhumika"]
    time.sleep(3)

    while True:
        name = (yield)
        if name in name_lst:
            print("Your name is present in this list")
        elif name=="e":
            print("Thanks for using this software, have a good day ahead..!")
        else:
            print("Your name is not present in this list")

search = search_name()
next(search)
while True:
    nm = input("Press e to exit or Enter Your Name to search :")
    search.send(nm)
    if nm=="e":
        exit()

search.close()
