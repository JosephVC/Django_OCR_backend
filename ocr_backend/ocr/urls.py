from django.urls import path

from .views import PostViews 

urlpatterns = [
    path('upload/', PostViews.as_view(), name='file-upload'),
]