from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListCreateView.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
]
