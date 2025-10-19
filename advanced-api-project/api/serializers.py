from .models import Author, Book
from rest_framework import serializers
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles the conversion of Book model instances to and from JSON format.
    It includes validation to ensure that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate(self, data):
        """
        Validates the publication year.
        """
        if data['publication_year'] > timezone.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer handles the conversion of Author model instances to and from JSON format.
    It includes a nested representation of the author's books using the BookSerializer.
    The 'books' field is a read-only field that gets its value from the reverse relationship
    on the Author model (book_set).
    """
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
