class Library:
    def __init__(self, listOfBooks, libraryName):
        self.books = listOfBooks
        self.name = libraryName
        self.lendDict = {}

    def displayAvailableBooks(self):
        print(f"Books preset in {self.name} Library are:")
        for index, book in enumerate(self.books):
            print(f"  {index+1}) {book}")

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated. You can take this book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}, please waite untill the book is available.")

    def addBook(self, book):
        self.books.append(book)
        print(f"Book has been successfully added to the {self.name} Library.")

    def returnBook(self, book):
        self.lendDict.pop(book)
        print(f"Book has been successfully return to the {self.name} Library.")

if __name__ == '__main__':
    harry = Library(["Python", "Clrs", "Django", "Algorithm", "The jangal Book"], "CodeWithHarry")
    # harry.displayAvailableBooks()

    while True:
        wlcmsg = f'''\n ====== Welcome to {harry.name} Library
        Please Choose an one option:
        1) List of Books
        2) Lend Book
        3) Add Book
        4) Return Book
        5) Exit
        '''
        print(wlcmsg)
        a = int(input("Enter a Choice: "))

        if a == 1:
            harry.displayAvailableBooks()

        elif a == 2:
            user_name = input("Enter User Name: ")
            book_name = input("Enter the book name: ")
            harry.lendBook(user_name, book_name)

        elif a == 3:
            book_name = input("Enter the book name: ")
            harry.addBook(book_name)

        elif a == 4:
            book_name = input("Enter the book name: ")
            harry.returnBook(book_name)

        elif a == 5:
            print(f"Thanks for using {harry.name} Library, Good day ahead...!")
            exit()

        else:
            print("Invalid Choice..!")