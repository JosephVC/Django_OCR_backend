from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Imaginary function for uploading a file
from foo import handle_uploaded_file
# this will likely be linked to the OCRMyPDF program

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        
        return render(request, 'upload.html', {'form':  form})
