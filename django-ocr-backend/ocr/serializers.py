from rest_framework import serializers

from .models import Post

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'
