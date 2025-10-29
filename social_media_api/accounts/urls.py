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
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='user-follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='user-unfollow'),
]
