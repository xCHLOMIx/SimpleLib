import json

with open('data.json', 'r') as openfile:
 
    # Reading from json file
    books = json.load(openfile)

users = []

name = input("Enter your name: \n👉 ")
def menu():
    user = {
        "name" : name,
        "books" : []
    }
    users.append(user)

    choice = input("Enter choice: \n(1) Create a new book \n(2) Borrow a book \n(3) Return a book \n(4) Check if a book is available \n(5) See all available books \n(6) Search for books \n(7) Save books as JSON \n(0) Exit \n👉 ")

    match choice:
        case '1':
            title = input("Enter title for the new book: \n👉 ")
            author = input("Enter author for the new book: \n👉 ")
            createNewBook(title, author)
        case '2':
            title = input("Enter book you want to borrow: \n👉 ")
            borrowBook(title)
        case '3':
            title = input("Enter book to return: \n👉 ")
            returnBook(title)
        case '4':
            title = input("Enter book to check: \n👉 ")
            checkAvailability(title)
        case '5':
            availableBooks()
        case '6':
            title = input("Search... \n👉 ")
            searchForBooks(title)
        case '7':
            saveAsJSON()
        case '0':
            print("Thanks for using our library ❤️")
        case _:
            print("Invalid input")
            menu()

# Function to create a new book
# It creates a new object book with the title given and it's availability set to available by default
def createNewBook(title, author):
    newBook = {
        "title": title,
        "author": author,
        "availability": "available"
    }

    books.append(newBook)
    print(f"Book '{title}' saved successfully 👌")
    menu()

# Function to borrow an existing book from the library
# It checks if that book is in the library and it's available to lend
def borrowBook(title):
    if len(books) <= 0:
        print("No books in the library 🙅‍♂️")
        menu()
    else:
        for book in books:
            if title == book['title']:
                if book['availability'] == "available":
                    users[0]['books'].append(book)
                    book['availability'] = 'borrowed'
                    print(f"{users[0]['name']}, You successfully borrowed the book '{title}' 👌")
                    menu()
                else:
                    for borrowed in users[0]['books']:
                        if title == borrowed['title']:
                            print(f"You already borrowed the book '{title}' 🙅‍♂️")
                            menu()
                        else:
                            print(f"Book '{title}' was borrowed 😔")
                            menu()
            else:
                print(f"No such book titled '{title}' 🙅‍♂️")
                menu()

# Function to rutern a book that you borrowed from the library
# It checks if that book is in the books of the user
def returnBook(title):
    if len(users[0]['books']) <= 0:
        print("You didn't borrow any books 🙅‍♂️")
        menu()
    else:
        for book in users[0]['books']:
            for book in books:
                if title == book['title']:
                    book['availability'] = 'available'
                else:
                    pass
            if title == book['title']:
                users[0]['books'].remove(book)
                print(f"Thanks for returning the book '{title}' ❤️")
                menu()
                continue
            else:
                print(f"You dont have the book '{title}' 🙅‍♂️")
                menu()

# Function to check it a certain book is available by using its title:
def checkAvailability(title):
    if len(books) <= 0:
        print("No books in the library 🙅‍♂️")
        menu()
    else:
        for book in books:
            if title == book['title']:
                if book['availability'] == "available":
                    print(f"The book '{title}' is available 👌")
                    menu()
                else:
                    print(f"The book '{title}' is not available 🙅‍♂️")
                    menu()
            else:
                print(f"No such book titled '{title}' 🙅‍♂️")
                menu()

# Function to check the books available in the library:
def availableBooks():
    if len(books) <= 0:
        print("No books in the library 🙅‍♂️")
        menu()
    else:
        for book in books:
            if book['availability'] == "available":
                print("Books 📚:")
                print(f"📕 Title: {book['title']} ✍️  Author: {book['author']} ⏲️  Availability: {book['availability'].capitalize() }")
            else:
                print("No available books 🙅‍♂️")
    menu()

# This is the function for searching for books using its title
def searchForBooks(title):
    if len(books) <= 0:
            print("No books in the library 🙅‍♂️")
            menu()
    else:
        for book in books:
            if title in book['title']:
                print("Books 📚:")
                print(f"📕 Title: {book['title']} ✍️  Author: {book['author']} ⏲️  Availability: {book['availability'].capitalize() }")
                continue
        print(f"No more results of '{title}' to be found 🙅‍♂️")
    menu()

# This is the function to save the book[] as JSON
def saveAsJSON():
    if len(books) <= 0:
        print("No books in the library 🙅‍♂️")
        menu()
    else:
        with open('data.json', 'w') as f:
            json.dump(books, f, indent=4)
        print("Check your folder 📁")
    menu()

menu()