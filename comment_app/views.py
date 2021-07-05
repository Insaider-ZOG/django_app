from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from . import serializers, models, permissions


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


class OneComment(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommentDetailDelete(mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentUpdate(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)