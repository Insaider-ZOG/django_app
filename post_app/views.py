from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import serializers, models, permissions


class CategoryList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryListSerializer


class CreatePost(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Post.objects.all()
    serializer_class = serializers.CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(creator_post=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostListSerializer


class GetOnePost(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostDetailDelete(mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostDetailUpdate(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)