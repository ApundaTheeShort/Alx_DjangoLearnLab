from .models import Author, Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate(self, data):

        if data['publication_year'] > 2024:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
