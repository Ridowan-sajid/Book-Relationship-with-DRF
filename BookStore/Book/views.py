from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import ListCreateAPIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer