from django.db import models

# Create your models here.


class Author(models.Model):
    """
    Represents an author entity.

    Attributes:
        name (str): The full name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book entity.

    Attributes:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (ForeignKey): A reference to the Author of the book.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
