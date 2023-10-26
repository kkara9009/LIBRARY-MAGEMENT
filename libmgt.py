import json

# Create a library database
library = {
    "books": [],
    "patrons": []
}

# Define book and patron classes
class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"

class Patron:
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number
        self.checked_out_books = []

    def __str__(self):
        return self.name

# Function to save library data to a JSON file
def save_library_data():
    with open("library_data.json", "w") as file:
        json.dump(library, file, indent=4)

# Function to load library data from a JSON file
def load_library_data():
    try:
        with open("library_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "books": [],
            "patrons": []
        }

# Initialize the library with data from the file, if available
library = load_library_data()

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Add a Patron")
    print("3. List Books")
    print("4. List Patrons")
    print("5. Check Out Book")
    print("6. Return Book")
    print("7. Save and Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        isbn = input("Enter the ISBN: ")
        book = Book(title, author, isbn)
        library["books"].append(book)
        save_library_data()
        print(f"{book} has been added to the library.")

    elif choice == "2":
        name = input("Enter the patron's name: ")
        card_number = input("Enter the patron's card number: ")
        patron = Patron(name, card_number)
        library["patrons"].append(patron)
        save_library_data()
        print(f"{patron} has been added to the library patrons.")

    elif choice == "3":
        for book in library["books"]:
            print(book)

    elif choice == "4":
        for patron in library["patrons"]:
            print(patron)

    elif choice == "5":
        card_number = input("Enter patron's card number: ")
        isbn = input("Enter book's ISBN: ")
        for patron in library["patrons"]:
            if patron.card_number == card_number:
                for book in library["books"]:
                    if book.ISBN == isbn and book.available:
                        book.available = False
                        patron.checked_out_books.append(book)
                        print(f"{book.title} has been checked out by {patron.name}.")
                        save_library_data()
                        break
                else:
                    print("Book not found or already checked out.")
                break
        else:
            print("Patron not found.")

    elif choice == "6":
        card_number = input("Enter patron's card number: ")
        isbn = input("Enter book's ISBN: ")
        for patron in library["patrons"]:
            if patron.card_number == card_number:
                for book in patron.checked_out_books:
                    if book.ISBN == isbn:
                        book.available = True
                        patron.checked_out_books.remove(book)
                        print(f"{book.title} has been returned by {patron.name}.")
                        save_library_data()
                        break
                else:
                    print("Book not found or not checked out by the patron.")
                break
        else:
            print("Patron not found.")

    elif choice == "7":
        print("Saving library data and exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
