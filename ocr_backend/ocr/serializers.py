from rest_framework import serializers

from .models import File

class OcrSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'file',
            'description',
            'timestamp',
        )
