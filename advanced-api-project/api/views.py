from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, serializers
from django.utils import timezone


class ListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books.

    This view handles GET requests and returns a list of all Book instances
    serialized using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by its ID.

    This view handles GET requests and returns a single Book instance
    serialized using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateView(generics.CreateAPIView):
    """
    API view to create a new book.

    This view handles POST requests and creates a new Book instance
    using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def validate(self, data):
        """
        Validates the publication year.
        """
        if data['publication_year'] > timezone.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return data


class CreateAuthorView(generics.CreateAPIView):
    """
    API view to create a new author.

    This view handles POST requests and creates a new Author instance
    using the AuthorSerializer.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.

    This view handles PUT requests and updates an existing Book instance
    using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def validate(self, data):
        """
        Validates the publication year.
        """
        if data['publication_year'] > timezone.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return data


class DeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.

    This view handles DELETE requests and deletes an existing Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
