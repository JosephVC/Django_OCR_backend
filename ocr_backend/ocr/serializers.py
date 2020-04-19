from rest_framework import serializers

from .models import OCRFile

class OcrSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = OCRFile