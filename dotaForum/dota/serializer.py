from rest_framework import serializers
from dota.models import User, Categories, Comment, Likes, Dislikes, Message, Post, Reply, Report


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class RegSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoriesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class DislikesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Dislikes
        fields = '__all__'

class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ReplySerializer (serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ReportSerializer (serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'