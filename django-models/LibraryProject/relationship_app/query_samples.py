from .models import Book, Library, Author, Librarian

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

library = Library.objects.get(name=library_name)
library_books = library.books.all()

get_library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=get_library)