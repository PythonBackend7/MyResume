from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'name', 'message', 'created_at']


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'category', 'tags', 'title', 'image', 'description', 'file', 'created_at', 'comments']
