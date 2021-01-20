from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
 
from django.conf import settings
from django.conf.urls.static import static

admin.site.header_title = 'OCR App Administration'
admin.site.site_title = 'OCR App Administration'

urlpatterns = [
    #OAuth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')), 
    # Project URLs
    # For security purposes, the stock '/admin/' url has been changed
    path('cynosure/', admin.site.urls),
    path('', include('ocr.urls', namespace='ocr')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # OCR API Application
    path('api/', include('ocr.urls', namespace='ocr_api')),
    
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)