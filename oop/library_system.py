class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size

    def __str__(self):
        return f"(EBook, Size: {self.file_size}MB)"
    
class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count

    def __str__(self):
        return f"(PrintBook, Pages: {self.page_count})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        self.books.append(Book)
    
    def list_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)
