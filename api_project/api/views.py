from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Set the authentication and permission classes for this view.
    # - TokenAuthentication: Clients must provide a valid token to authenticate.
    # - IsAuthenticated: Only authenticated users can access this view.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Set the authentication and permission classes for this viewset.
    # - TokenAuthentication: Clients must provide a valid token to authenticate.
    # - IsAdminUser: Only users with admin privileges can access this viewset.
    # - IsAuthenticated: Only authenticated users can access this viewset.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
