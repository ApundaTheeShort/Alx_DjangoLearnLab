from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
# from .import admin_view

urlpatterns = [
    # path("", views.home, name="home"),
    path("list_books/", views.list_books, name="list_books"),
    path("library_details/", views.LibraryDetailView.as_view(), name="library_details"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),
]