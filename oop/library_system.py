class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size

class PrintBook(book):
    def __init__(self, page_count):
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        self.books.append(book)
    
    def list_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)
