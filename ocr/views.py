from django.http import FileResponse, HttpResponse
# from rest_framework.views import APIView
<<<<<<< HEAD
from rest_framework.generics import ListAPIView
=======
from rest_framework.generics import CreateAPIView, ListAPIView
>>>>>>> ab93cae9d66fb37008bf3ffa4359f18dc75618bb
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE, STDOUT

import ocrmypdf
import os

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

# class PostViews(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = FileSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
        
#         posts_serializer = FileSerializer(data=request.data)
#         if posts_serializer.is_valid():
                     
#             # The below removes the necessity to hard-code the path to the input file.
#             uploaded = posts_serializer.save()  
            
#             process = Popen(['ocrmypdf', uploaded.file.path, 'output.pdf'])

#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)

#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)