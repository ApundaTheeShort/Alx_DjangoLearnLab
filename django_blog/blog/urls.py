from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('post/<int:pk>/comments/new/',
         CommentCreateView.as_view(), name='comments-create'),
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search, name='search'),
    path('tag/<slug:tag_slug>/', views.tagged, name='tagged'),
]
