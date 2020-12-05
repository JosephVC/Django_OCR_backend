from django.urls import path, include

from . import views
from .views import PostViews

app_name = 'ocr_api'

urlpatterns = [
    path('', PostViews.as_view(), name='file-upload'),
   
]