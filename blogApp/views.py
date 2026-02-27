from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User

# ---------  with viewsets  -------------------
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.select_related('author')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("No Permission to update the data")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('No permission to perform delete')
        instance.delete()



# -----------   with APIVIEW  ------------------
class BlogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.select_related("author")
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BlogRetiveUpdateDeleteView(APIView):
    def get_object(self, id):
        return get_object_or_404(Blog, id=id)
    
    def get(self, request, id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request, id):
        blog = self.get_object(id)

        if blog.author != request.user:
            return Response({
                'error': "Not allowed to update the data"
            }, status = status.HTTP_403_FORBIDDEN)

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        blog = self.get_object(id)
        if blog.author != request.user:
            return Response({
                'error': "Not allowed to delete the data"
            }, status = status.HTTP_403_FORBIDDEN)
        blog.delete()
        return Response({
                'message': "Deleted Successfully"
            }, status = status.HTTP_204_NO_CONTENT)

