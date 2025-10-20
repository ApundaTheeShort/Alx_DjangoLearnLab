from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, serializers
from django.utils import timezone
from django_filters import rest_framework as filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookFilter(filters.CharFilter):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    publication_year = filters.NumberFilter(field_name='publication_year')
    author = filters.CharFilter(
        field_name='author__name', lookup_expr='icontains')


class ListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books.

    This view handles GET requests and returns a list of all Book instances
    serialized using the BookSerializer.

    **Filtering, Searching, and Ordering:**

    This view supports filtering, searching, and ordering of the results.

    **Filtering:**
    - Filter by publication year: `?publication_year=<year>`
    - Example: `?publication_year=2023`

    **Searching:**
    - Search by title and author: `?search=<term>`
    - Example: `?search=Django`

    **Ordering:**
    - Order by publication year, title, or author: `?ordering=<field>`
    - Prepend the field with a `-` for descending order.
    - Example (ascending by title): `?ordering=title`
    - Example (descending by publication year): `?ordering=-publication_year`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['publication_year', 'title', 'author']
    search_fields = ['title', 'author']
    filterset_class = BookFilter
    filter_backends = [filters.OrderingFilter]


class DetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by its ID.

    This view handles GET requests and returns a single Book instance
    serialized using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateView(generics.CreateAPIView):
    """
    API view to create a new book.

    This view handles POST requests and creates a new Book instance
    using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.

    This view handles PUT requests and updates an existing Book instance
    using the BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'author']

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
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'author']
