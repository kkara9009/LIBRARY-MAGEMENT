from datetime import datetime, timedelta

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = {}
        self.lend_data = {}

    def display_books(self):
        if self.books:
            for index, book in enumerate(self.books, 1):
                if book["title"] in self.lend_data:
                    due_date = self.lend_data[book["title"]]
                    status = f" (Lent to: {due_date})"
                else:
                    status = " (Available)"
                print(f'({index}) {book["title"]} by {book["author"]}{status}')
        else:
            print("No books available in the library.")
        print()

    def add_book(self, title, author, genre, isbn):
        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "isbn": isbn,
        }
        self.books.append(book)
        print(f"{title} by {author} has been added to the library.\n")

    def lend_book(self, user_name, book_title, due_date):
        for book in self.books:
            if book["title"].lower() == book_title.lower():
                if book_title not in self.lend_data:
                    self.lend_data[book_title] = (user_name, due_date)
                    print(f"{book_title} has been lent to {user_name} until {due_date}.\n")
                else:
                    print(f"{book_title} is already lent to {self.lend_data[book_title][0]} until {self.lend_data[book_title][1]}.\n")
                return
        print(f"{book_title} is not available in the library.\n")

    def return_book(self, book_title):
        if book_title in self.lend_data:
            self.lend_data.pop(book_title)
            print(f"{book_title} has been returned.\n")
        else:
            print(f"{book_title} is not marked as lent.\n")

    def create_user(self, user_name, user_email):
        self.users[user_name] = user_email
        print(f"User {user_name} has been created with email {user_email}.\n")

    def view_users(self):
        for user, email in self.users.items():
            print(f"User: {user}, Email: {email}")
        print()

def main():
    library_name = "My Library"
    library = Library(library_name)

    while True:
        print(f"Welcome to {library_name}")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Create a user")
        print("6. View users")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, genre, isbn)
        elif choice == "3":
            user_name = input("Enter your name: ")
            book_title = input("Enter the title of the book you want to lend: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            library.lend_book(user_name, book_title, due_date)
        elif choice == "4":
            book_title = input("Enter the title of the book you are returning: ")
            library.return_book(book_title)
        elif choice == "5":
            user_name = input("Enter a new user's name: ")
            user_email = input("Enter the user's email: ")
            library.create_user(user_name, user_email)
        elif choice == "6":
            library.view_users()
        elif choice == "7":
            print("Thank you for using the library. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
