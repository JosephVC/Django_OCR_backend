from django.urls import path, include

from . import views
from .views import PostViews

urlpatterns = [
    path('', PostViews.as_view(), name='file-upload'),
   
]