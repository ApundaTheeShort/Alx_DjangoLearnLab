from django.urls import path
from.views import BookView, LibraryBookView

urlpatterns = [
    path("list_books/", BookView, name="list_books"),
    path("library_details/", LibraryBookView.as_view(), name="library_details"),
]