from rest_framework import serializers
from .models import CustomUser, Post
from taggit.serializers import TagListSerializerField, TaggitSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'
