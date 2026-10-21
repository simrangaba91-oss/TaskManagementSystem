def search_book(books, title):
    for book in books:
        if title.lower() in book.lower():
            return book
    return None


if __name__ == "__main__":
    books = [
        "Python Programming",
        "Introduction to Algorithms",
        "Data Structures",
        "Database Management"
    ]

    title = input("Enter book title to search: ")
    result = search_book(books, title)

    if result:
        print("Book found:", result)
    else:
        print("Book not found.")