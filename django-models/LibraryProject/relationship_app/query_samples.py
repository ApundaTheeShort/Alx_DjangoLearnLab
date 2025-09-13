from .models import Book, Library

books = Book.objects.filter(author="Mike Dane")

library = Library.objects.get(name="Main Library")
library_books = library.books.all()

library = Library.objects.get(name="Main Library")
librarian = library.librarian
