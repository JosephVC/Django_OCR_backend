from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostDetail, PostViews

app_name = 'ocr_api'


urlpatterns = [
    path('', PostViews.as_view(), name='file-upload'),
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate')
]