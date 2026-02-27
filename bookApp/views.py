from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .models import Book
from .serializers import BookSerializers
from rest_framework.viewsets import ModelViewSet

from django.db.models import Q


# Create your views here.
class BookListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search = request.GET.get('search')
        books = Book.objects.select_related("author")

        if search:
            books = Book.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        book = get_object_or_404(Book, pk=pk)
        if book.author != user:
             raise PermissionDenied("You are not allowed to access this book")
        return book
    
    def get(self, request, pk):
        book = self.get_object(pk, request.user)
        serializer = BookSerializers(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk, request.user)
        if not book:
            return Response({"error": "Not allowed to update this book."}, status=status.HTTP_403_FORBIDDEN)

        serializer = BookSerializers(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        book = self.get_object(pk, request.user)
        if not book:
            return Response({"error": "Not allowed to delete this book"}, status=status.HTTP_403_FORBIDDEN)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# ---------------  using viewsets -------------------
class BookDetailsView(ModelViewSet):
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied('No Permission to update the data')
        return serializer.save()
    
    
    def perform_destroy(self, instance):
        if instance.author != request.user:
            return PermissionDenied('No permission to perform delete')
        instance.delete()
        




