from .models import Book, Library, Author

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

library = Library.objects.get(name=library_name)
library_books = library.books.all()

library = Library.objects.get(name=library_name)
librarian = library.librarian
