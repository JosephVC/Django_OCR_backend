from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'file',
            'description',
            'timestamp',
        )
