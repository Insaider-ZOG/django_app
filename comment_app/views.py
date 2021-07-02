from django.http import Http404
from rest_framework import generics, mixins, views, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from . import serializers, models, permissions


class OneCommentDetail(views.APIView):
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, pk):  # Зачем нужно было переопределять этот метод, ничего нового ты вроде не добавил
        try:
            return models.Comment.objects.get(pk=pk)
        except models.Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk): # Можно было использовать RetrieveModelMixin
        post = self.get_object(pk)
        serialiser = serializers.CommentListSerializer(post)
        return Response(serialiser.data)

    def delete(self, request, pk): # Можно было использовать DestroyModelMixin
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentUpdate(views.APIView):
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, pk):
        try:
            return models.Comment.objects.get(pk=pk)
        except models.Comment.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = serializers.CommentDetailSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateComment(mixins.CreateModelMixin,
               generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CreateCommentSerializer

    def perform_create(self, serializer):
        serializer.save(creator_comment=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
