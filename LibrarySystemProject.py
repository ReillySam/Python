####### ----- LIBRARY SYSTEM ----- #######
'''Create and implement a library system using dictionaries'''

#'''Implement a small library of 3 books using a Python dictionary.
# • Implement a Python function to print details about all books in the library.
# • Implement a Python function that adds a book to the library.
# Your function should ask for the book ISBN, title, author and how many copies
# have been purchased. The function should update the library inventory (the
# dictionary) to include the new book.
# If the book is already in the library the system should update the quantity.
# • Implement a Python function that checks out a book for loaning.
# • Implement a Python function that searches the library for a book by the book
# title and returns the book’s ISBN
# (Note: Assume that for every book title there is only one corresponding ISBN)'''


# dictionary containing all books in library, keyed by ISBN, value is a list = "book"
library = {1000000000001: ["The Tipping Point", "Malcolm Gladwell", 5, 5],
           1000000000002: ["The Picture of Dorian Gray", "Oscar Wilde", 5, 5],
           1000000000003: ["1984", "George Orwell", 5, 5]}

### ---- USER INPUTS  --- ###
def take_inputs(): #taking user inputs
    isbn = read_isbn()
    qty = 0
    name = input("Enter the book's title: ")
    author = input("Enter the author's name: ")

    while True:
        try:
            input_val = input("Please enter number of copies: ")
            qty = int(input_val)
            break
        except Error as e:
            print("Error reading quantity input: {0}".format(e))

    return [isbn, name, author, qty]

### ---- ADD BOOK FUNCTION --- ###
def add_to_library(isbn, title, author, quantity):
    try:
        if isbn in library:
            print("This ISBN already exists in the library. Please try again.")
        else:
            book = [title, author, quantity, quantity]
            library[isbn] = book
            print("Added book to library. Thank you!")
    except Error as e:
        print(e)

### ---- OPEN LIBRARY FUNCTION  --- ###
def print_library_details():
    print(" ----- Sam's Library ----- \n")

    for kvp in library.items():  # iterate key value pairs of books dictionary
        isbn = kvp[0]  # isbn is the first item (key)
        book = kvp[1]  # book list is the second item (value)

        print("ISBN: {0}: Title - {1}; Author - {2}; Quantity ({3}) / Stock ({4}) \n".format(isbn, book[0], book[1],
                                                                                                book[2], book[3]))

### ---- LOAN BOOK FUNCTION  --- ###
def loan_book(title):
    isbn = find_book(title)  # get isbn of book being loaned
    if isbn != -1: #check if isbn is valid, error check
        book = library[isbn]

        if book[3] == 0:
            print("Unfortunately all copies of the book ({0}) are already loaned out, unable to loan it at this time".format(book[0]))
            return

        book[3] = book[3] - 1
        print("Successfully loaned book, enjoy!")

### ---- RETURN BOOK FUNCTION  --- ###
def return_book(title):
    isbn = find_book(title)
    if isbn != -1:
        book = library[isbn]

        if book[2] == book[3]:
            print("All copies of book ({0}) already in library, can't return book".format(book[0]))
            return
        book[3] = book[3] + 1
        print("Successfully returned book, thank you!")

### ---- SEARCH BOOK FUNCTION  --- ###
def search_book(title):
    for kvp in library.items():  # iterate across library for keys and values
        isbn = kvp[0]
        book = kvp[1]

        if title == book[0].lower(): #title is first element in book list, check to see if they're a match
            print ("The ISBN for our book '{0}' is {1}.".format(book[0], isbn))
            break
    else:
        print("No book found under '{0}', please check the spelling.".format(title))

### ---- Find book function used to call book details in other functions --- ###
def find_book(title):
    isbn = 0  # set to 0 as default

    for kvp in library.items():#iterate across library
        isbn = kvp[0]
        book = kvp[1]

        if title == book[0].lower():  # if this book's title equals to one being searched for, assign isbn
            return isbn

    else:
        print("no book found with title {0}".format(title))#print error
        return -1

### ---- ISBN digit count check --- ###
def read_isbn():
    while True:
        isbn_str = input("please enter ISBN: ")
        length = len(isbn_str)
        if length != 13:
            print("The ISBN should be 13 digits, check again.")
        else:
            try:
                isbn = int(isbn_str)
                return isbn
            except Error as e:
                print("can't define that input ({0}), exception: {1}".format(isbn_str, e))

### ---- MENU --- ###
if __name__ == '__main__':  #main menu of library, takes user inputs and calls function
    print("---- Hello! Welcome to the Sam's library!! ----")

    while True:# user menu options
        input_val = input("\n--- MENU --- Enter one of the options below; "
                          "\n-open library \n-search book \n-loan book \n-return book \n-add book \n-exit? >> ")

        if input_val == "open library":
            print_library_details()

        elif input_val == "search book":
            title = input("Enter the title of the book you're looking for: ")
            search_book(title)

        elif input_val == "loan book":
            title = input("Enter title to loan: ")
            loan_book(title)

        elif input_val == "return book":
            title = input("Enter title to return: ")
            return_book(title)

        elif input_val == "add book":
            inputs = take_inputs()
            add_to_library(inputs[0], inputs[1], inputs[2], inputs[3])

        elif input_val == "exit":
            print("----- Exiting library, Goodbye!!-----")
            break
        else:
            print("No valid option chosen.")
