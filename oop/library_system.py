class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook, Size: {self.file_size}MB)"
    
class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (PrintBook, Pages: {self.page_count})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        self.books.append(Book)
    
    def list_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)
