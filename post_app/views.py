from django.http import Http404
from rest_framework import generics, mixins, views, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from . import serializers, models, permissions


class CategoryList(generics.ListAPIView): # Тут и ниже базовый CRUD либо его часть, можно было бы просто отнаследоваться от миксинов (CreateModelMixin, ...)
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryListSerializer


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostListSerializer


class OnePostDetail(views.APIView):
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, pk):
        try:
            return models.Post.objects.get(pk=pk)
        except models.Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serialiser = serializers.PostDetailSerializer(post)
        return Response(serialiser.data)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostUpdate(views.APIView):
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, pk):
        try:
            return models.Post.objects.get(pk=pk)
        except models.Post.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = serializers.PostDetailSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatePost(mixins.CreateModelMixin,
               generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = models.Post.objects.all()
    serializer_class = serializers.CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(creator_post=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
