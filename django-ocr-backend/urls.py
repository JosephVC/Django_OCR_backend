from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #OAuth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')), 
    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('ocr.urls', namespace='ocr')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # OCR API Application
    path('api/', include('ocr.urls', namespace='ocr_api')),
    
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)