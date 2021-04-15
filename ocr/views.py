# Python and Django-specific imports 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
import json
import os
from rest_framework import filters, generics, status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import ( SAFE_METHODS, IsAuthenticated, 
    IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, 
    DjangoModelPermissions ) 
from rest_framework.response import Response

#import needed for working with files
from subprocess import Popen

from urllib.parse import urlencode

# Import ocrmypdf, which does the heavy lifting regarding OCR
# Note that ocrmypdf is installed in a virtual environment with Poetry
import ocrmypdf

# Files local to the project
from ocr.serializers import FileSerializer
from .models import Post


class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()


# The view showing us the details of individual posts
class PostDetail(generics.RetrieveAPIView):

    serializer_class = FileSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

# This will allow us to search

class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = FileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

# Post Admin

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        posts_serializer = FileSerializer(data=request.data)
        
        if posts_serializer.is_valid():
                     
            # The below removes the necessity to hard-code the path to the input file.
            uploaded = posts_serializer.save()  

            # OCR component
            ocr_pdf = Popen(['ocrmypdf', uploaded.file.path, 'output.pdf'])

            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)

        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return uploaded


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = FileSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()