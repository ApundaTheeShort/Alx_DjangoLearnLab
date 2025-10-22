from django.urls import path
from . import views
from .views import CreateView, UpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', views.CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='post-detail'),
]
