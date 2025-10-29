from django.urls import path
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView,
    FollowUserView,
    UnfollowUserView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('users/<int:pk>/follow/', FollowUserView.as_view(), name='user-follow'),
    path('users/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='user-unfollow'),
]
