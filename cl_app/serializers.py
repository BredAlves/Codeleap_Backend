from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'username', 'created_datetime', 'title', 'content', 'author_ip')
        read_only_fields = ('id', 'username', 'created_datetime', 'author_ip')