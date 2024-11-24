from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Topic, Comment, Reply
from .serializers import TopicSerializer, CommentSerializer, ReplySerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class TopicListCreateAPIView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        return topic.comments.all()

    def perform_create(self, serializer):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        serializer.save(author=self.request.user, topic=topic)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        return topic.comments.all()


class ReplyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['comment_pk'])
        return comment.replies.all()

    def perform_create(self, serializer):
        comment = get_object_or_404(Comment, pk=self.kwargs['comment_pk'])
        serializer.save(author=self.request.user, comment=comment)


class ReplyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['comment_pk'])
        return comment.replies.all()
