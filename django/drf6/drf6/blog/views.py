from rest_framework import generics
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related("tags").all()
    serializer_class = PostSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related("tags").all()
    serializer_class = PostSerializer
    lookup_field = "pk"


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"
