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
    DjangoModelPermissions) 
from rest_framework.response import Response

#import needed for working with files
from subprocess import Popen, PIPE, STDOUT

from urllib.parse import urlencode

# Import ocrmypdf, which does the heavy lifting regarding OCR
# Note that ocrmypdf is installed in a virtual environment with Poetry
import ocrmypdf

# Files local to the project
from .serializers import FileSerializer
from .models import Post



# Post Search

# class PostListDetailfilter(generics.ListAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user 

# Note: everything seems to run fine without PostList, so I'll leave it out for now

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = FileSerializer
#     queryset = Post.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     # define custom queryset
#     def get_queryset(self):
#         return Post.objects.all()

# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self, request):
#         serializer_class = FileSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = FileSerializer(post)
#         return Response(serializer_class.data)

class PostDetail(generics.RetrieveAPIView, PostUserWritePermission):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = FileSerializer

    def get_object(self, queryset=None, **kwargs):
        item =  self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

class PostViews(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # parser_classes = (MultiPartParser, FormParser)

    queryset = Post.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item) 

    def get_queryset(self):
        return Post.objects.all()

    # def get(self, request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     serializer = FileSerializer(posts, many=True)
    #     return Response(serializer.data)

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

# class AdminPostDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class EditPost(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class DeletePost(generics.RetrieveDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()