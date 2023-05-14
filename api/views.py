from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly


class DetailViewSet(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateViewSet(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
