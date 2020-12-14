from django.urls import path

from .views import ( PostDetail, PostViews, PostListDetailfilter, 
    CreatePost, AdminPostDetail, EditPost, DeletePost )

app_name = 'ocr_api'


urlpatterns = [
    path('', PostViews.as_view(), name='file-upload'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    # Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(),
        name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost')

]