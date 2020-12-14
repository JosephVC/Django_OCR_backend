# Python and Django-specific imports 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
import json
import os
from rest_framework import filters, generics, status, viewsets 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import ( SAFE_METHODS, IsAuthenticated, 
    IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, 
    DjangoModelPermissions ) 
from rest_framework.response import Response

#import needed for working with files
from subprocess import Popen, PIPE, STDOUT

from urllib.parse import urlencode

# Import ocrmypdf, which does the heavy lifting regarding OCR
# Note that ocrmypdf is installed in a virtual environment with Poetry
import ocrmypdf

# Files local to the project
from ocr.serializers import FileSerializer
from ocr.models import Post


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user 

class PostViews(generics.ListAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FileSerializer
    queryset = Post.objects.all()
    
    def post(self, request, *args, **kwargs):
        
        posts_serializer = FileSerializer(data=request.data)
        if posts_serializer.is_valid():
                     
            # The below removes the necessity to hard-code the path to the input file.
            uploaded = posts_serializer.save()  
            
            process = Popen(['ocrmypdf', uploaded.file.path, 'output.pdf'])

            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)

        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return uploaded
    
    def delete(self, request, uploaded, format=None):
        uploaded.posts_serializer.delete(save=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


# The view showing us the details of individual posts
class PostDetail(generics.RetrieveAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Post.objects.filter(slug=slug)


class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = FileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

# Post Admin

class CreatePost(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()


class AdminPostDetail(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = FileSerializer

class EditPost(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = Post.objects.all()