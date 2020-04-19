from rest_framework import generics

from .models import OCRFile
from .serializers import OcrSerializer

class ListOcr(generics.ListCreateAPIView):
    queryset = OCRFile.objects.all()
    serializer_class = OcrSerializer

class DetailOcr(generics.RetrieveUpdateDestroyAPIView):
    queryset = OCRFile.objects.all()
    serializer_class = OcrSerializer
    