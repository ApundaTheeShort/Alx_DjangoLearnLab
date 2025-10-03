import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- Create Sample Data ---

    # Create Authors
    author1, _ = Author.objects.get_or_create(name="J.K. Rowling")
    author2, _ = Author.objects.get_or_create(name="George R.R. Martin")

    # Create Books
    book1, _ = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2, _ = Book.objects.get_or_create(title="A Game of Thrones", author=author2)
    book3, _ = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)

    # Create a Library
    library1, _ = Library.objects.get_or_create(name="Downtown Library")
    library1.books.add(book1, book2)

    # Create a Librarian
    librarian1, _ = Librarian.objects.get_or_create(name="John Doe", library=library1)

    print("--- Sample Data Created ---")
    print(f"Authors: {list(Author.objects.all())}")
    print(f"Books: {list(Book.objects.all())}")
    print(f"Libraries: {list(Library.objects.all())}")
    print(f"Librarians: {list(Librarian.objects.all())}")
    print("-" * 20)


    # --- Run Queries ---

    # 1. Query all books by a specific author (J.K. Rowling)
    print("1. Books by J.K. Rowling:")
    books_by_author = Book.objects.filter(author__name="J.K. Rowling")
    for book in books_by_author:
        print(f"- {book.title}")
    print("-" * 20)


    # 2. List all books in a library (Downtown Library)
    print("2. Books in Downtown Library:")
    library_to_check = Library.objects.get(name="Downtown Library")
    books_in_library = library_to_check.books.all()
    for book in books_in_library:
        print(f"- {book.title}")
    print("-" * 20)


    # 3. Retrieve the librarian for a library (Downtown Library)
    print("3. Librarian for Downtown Library:")
    library_to_find_librarian = Library.objects.get(name="Downtown Library")
    librarian = Librarian.objects.get(library=library_to_find_librarian)
    # Or more directly: librarian = library_to_find_librarian.librarian
    print(f"- {librarian.name}")
    print("-" * 20)

if __name__ == "__main__":
    run_queries()