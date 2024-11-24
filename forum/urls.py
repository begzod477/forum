# urls.py
from django.urls import path
from .views import (
    TopicListCreateAPIView, TopicDetailAPIView, 
    CommentListCreateAPIView, CommentDetailAPIView,
    ReplyListCreateAPIView, ReplyDetailAPIView
)

urlpatterns = [
    path('topics/', TopicListCreateAPIView.as_view(), name='topic-list-create'),
    path('topics/<int:pk>/', TopicDetailAPIView.as_view(), name='topic-detail'),
    path('topics/<int:topic_pk>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('topics/<int:topic_pk>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('comments/<int:comment_pk>/replies/', ReplyListCreateAPIView.as_view(), name='reply-list-create'),
    path('comments/<int:comment_pk>/replies/<int:pk>/', ReplyDetailAPIView.as_view(), name='reply-detail'),
]
