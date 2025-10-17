from django.urls import path, include
from .views import BookViewSet
from .views import BookList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books_all', BookViewSet, basename='books_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)s
    # This includes all routes registered with the router
    path('', include(router.urls)),
]
