from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("list_books/", list_books, name="list_books"),
    path("library_details/", LibraryDetailView.as_view(), name="library_details"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.Register.as_view(template_name="relationship_app/register.html"), name="register"),
]