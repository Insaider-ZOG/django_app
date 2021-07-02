from rest_framework import serializers

from .models import Post, Category


class CategoryListSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['id', 'category_name', 'posts', 'time_create', 'comments']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    creator_post = serializers.ReadOnlyField(source='creator_post.username')
    category = serializers.ReadOnlyField(source='category.category_name')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'creator_post', 'description', 'category', 'is_published', 'comments']


class CreatePostSerializer(serializers.ModelSerializer):
    creator_post = serializers.ReadOnlyField(source='creator_post.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'creator_post', 'description', 'category', 'is_published']
        read_only_field = ['creator_post']


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'