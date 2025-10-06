from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.book_list, name="book_list"),
    path("book_details/<int:book_id>/", views.book_details, name="book_details"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
