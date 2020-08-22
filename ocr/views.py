from django.http import FileResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE, STDOUT

import ocrmypdf
import os

from .serializers import FileSerializer
from .models import Post

ACCESS_KEY_ID = os.environ.get('')
ACCESS_SECRET_KEY = os.environ.get('')
BUCKET_NAME = ''

class PostViews(APIView):
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

            # now that weve uploaded and processed our pdf, 
            # it's time to send it of to the AWS bucket

            s3 = boto3.resources('s3',
                aws_access_key = ACCESS_KEY_ID,
                aws_secret_access_key = ACCESS_SECRET_KEY)

        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    