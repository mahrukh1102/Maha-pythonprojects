import os
import json

LIBRARY_FILE = "library.txt"

# Preload books
PRELOADED_BOOKS = [
    {
        "title": "Jannat Kay Pattay",
        "author": "Nemrah Ahmed",
        "year": 2012,
        "genre": "Romance / Thriller",
        "read": True
    },
    {
        "title": "Haalim",
        "author": "Nemrah Ahmed",
        "year": 2017,
        "genre": "Fantasy / Politics",
        "read": False
    },
    {
        "title": "Namal",
        "author": "Nemrah Ahmed",
        "year": 2014,
        "genre": "Crime / Thriller",
        "read": True
    },
    {
        "title": "Mushaf",
        "author": "Nemrah Ahmed",
        "year": 2011,
        "genre": "Spiritual / Mystery",
        "read": False
    }
]

# Load library / preload books 
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    else:
        return PRELOADED_BOOKS.copy()

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Display menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title/author: ").lower()

    found_books = []
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            found_books.append(book)

    if found_books:
        print("Matching Books:")
        for i, book in enumerate(found_books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_count = sum(book['read'] for book in library)
    percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Main program
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()