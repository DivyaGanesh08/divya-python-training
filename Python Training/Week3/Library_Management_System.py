
class LibraryItem():

    def __init__(self, title):
        self.title = title
    def issue(self):
        pass

class Book(LibraryItem):

    def issue(self):
        return f"Book '{self.title}' issued for 14 days"

book_name = input("Enter Book Name: ")
book = Book(book_name)
print(book.issue())