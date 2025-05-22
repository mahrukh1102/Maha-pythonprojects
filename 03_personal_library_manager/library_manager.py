import streamlit as st
import os
import json

LIBRARY_FILE = "library.txt"
PRELOADED_BOOKS = []

def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                content = file.read().strip()
                if not content:
                    return PRELOADED_BOOKS.copy()
                return json.loads(content)
        except json.JSONDecodeError:
            st.warning(f"{LIBRARY_FILE} is not valid JSON. Starting with empty library.")
            return PRELOADED_BOOKS.copy()
    else:
        return PRELOADED_BOOKS.copy()

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    st.header("Add a Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        if not (title and author and genre):
            st.error("Please fill in all fields.")
            return library
        new_book = {
            "title": title.strip(),
            "author": author.strip(),
            "year": year,
            "genre": genre.strip(),
            "read": read
        }
        library.append(new_book)
        save_library(library)
        st.success(f"Added '{title}' to the library.")
    return library

def remove_book(library):
    st.header("Remove a Book")
    if not library:
        st.info("No books in the library to remove.")
        return library
    titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove", options=titles)

    if st.button("Remove Book"):
        library = [book for book in library if book["title"] != book_to_remove]
        save_library(library)
        st.success(f"Removed '{book_to_remove}' from the library.")
    return library

def search_books(library):
    st.header("Search Books")
    search_by = st.radio("Search by", ("Title", "Author"))
    keyword = st.text_input(f"Enter {search_by} keyword")

    if keyword:
        keyword_lower = keyword.lower()
        results = [book for book in library if keyword_lower in book[search_by.lower()].lower()]
        if results:
            st.write(f"Found {len(results)} book(s):")
            for book in results:
                read_status = "Read" if book["read"] else "Unread"
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) — {book['genre']} — {read_status}")
        else:
            st.warning("No matching books found.")

def display_all_books(library):
    st.header("All Books in Library")
    if not library:
        st.info("Library is empty.")
        return
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['year']}) — {book['genre']} — {read_status}")

def show_statistics(library):
    st.header("Library Statistics")
    total = len(library)
    if total == 0:
        st.info("No books in the library.")
        return
    read_count = sum(book["read"] for book in library)
    percentage = (read_count / total) * 100
    st.write(f"Total books: {total}")
    st.write(f"Books read: {read_count}")
    st.write(f"Percentage read: {percentage:.1f}%")

def main():
    st.title("📚 Personal Library Manager")

    library = load_library()

    menu = ["Add Book", "Remove Book", "Search Book", "Display All Books", "Statistics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        library = add_book(library)
    elif choice == "Remove Book":
        library = remove_book(library)
    elif choice == "Search Book":
        search_books(library)
    elif choice == "Display All Books":
        display_all_books(library)
    elif choice == "Statistics":
        show_statistics(library)

    save_library(library)

if __name__ == "__main__":
    main()
