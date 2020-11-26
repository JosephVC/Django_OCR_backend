# Python and Django-specific imports 
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
import json
import os
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE, STDOUT
from urllib.parse import urlencode

# Import ocrmypdf, which does the heavy lifting regarding OCR
# Note that ocrmypdf is installed in a virtual environment with Poetry
import ocrmypdf

# Files local to the project
from .serializers import FileSerializer
from .models import Post


class PostViews(ListAPIView):
    serializer_class = FileSerializer
    queryset = Post.objects.all()

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = FileSerializer(posts, many=True)
        return Response(serializer.data)

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

