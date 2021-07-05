from rest_framework import serializers

from comment_app.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    creator_comment = serializers.ReadOnlyField(source='creator_comment.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id', 'creator_comment', 'post', 'description', 'time_create', 'time_update']


class CreateCommentSerializer(serializers.ModelSerializer):
    creator_comment = serializers.ReadOnlyField(source='creator_comment.username')

    class Meta:
        model = Comment
        fields = ['id', 'creator_comment', 'post', 'description']


class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'