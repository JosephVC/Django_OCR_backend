from django.http import FileResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE, STDOUT

import boto3
from botocore.client import Config
import ocrmypdf
import os

from .serializers import FileSerializer
from .models import Post

ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID', 'AWS_ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('AWS_S3_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'heroku-backend-bucket'

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

            data = open('output.pdf', 'rb')

            s3 = boto3.resource(
                's3',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY,
                config=Config(signature_version='s3v4')
            )
            s3.Bucket(BUCKET_NAME).put_object(Key='media/output.pdf', Body=data)

        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    