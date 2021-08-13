class Library:
    def __init__(self, ListOfBooks):
        self.books = ListOfBooks

    def displayAvailableBooks(self):
        print("Books available in this library are:")
        for index, book in enumerate(self.books):
            print(f"  {index+1}) {book}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"You have isshued {bookName} book. Please keep it safe and return it within 30 days")
            return True
        else:
            print("Sorry this book is ether not available or has already been isshued to someone else, please waite untill the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for adding/returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to add/return: ")
        return self.book

if __name__ == '__main__':
    central_library = Library(["Python", "Algorithm", "Clrs", "Django"])
    student1 = Student()
    # central_library.displayAvailableBooks()

    while True:
        wlcmsg = '''\n======== Welcome to Central Library ========
        Please choose an one option:
        1) List of all Books
        2) Borrow Book
        3) Return/Add Book
        4) Exit'''
        print(wlcmsg)
        a = int(input("\nEnter a Choice: "))

        if a==1:
            central_library.displayAvailableBooks()

        elif a==2:
            central_library.borrowBook(student1.requestBook())

        elif a==3:
            central_library.returnBook(student1.returnBook())

        elif a==4:
            print("Thanks for using Central Library..!, Good Day ahead...!")
            exit()

        else:
            print("Invalid Choice..!")
