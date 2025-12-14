from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post, Like, Comment, Follow, Notification, UserProfile, Story

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'profile_picture_url']

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    is_following = serializers.SerializerMethodField()
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'followers_count', 'following_count', 'posts_count', 'is_following', 'profile']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

    def get_posts_count(self, obj):
        return obj.posts.count()
    
    def get_is_following(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated and request.user != obj:
            return Follow.objects.filter(follower=request.user, following=obj).exists()
        return False

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            data['user'] = user
        return data

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    comments = CommentSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()
    image_display_url = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'image', 'image_url', 'image_display_url', 'caption', 'user', 'created_at', 
                 'likes_count', 'comments_count', 'comments', 'is_liked']

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Like.objects.filter(user=request.user, post=obj).exists()
        return False

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image', 'caption']
    
    def validate(self, data):
        if not data.get('image'):
            raise serializers.ValidationError("Image file is required")
        return data

class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image_display_url = serializers.ReadOnlyField()
    is_expired = serializers.ReadOnlyField()

    class Meta:
        model = Story
        fields = ['id', 'image', 'image_url', 'image_display_url', 'text', 'user', 'created_at', 'expires_at', 'is_expired']

class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['image', 'text']
    
    def validate(self, data):
        if not data.get('image'):
            raise serializers.ValidationError("Image file is required")
        return data

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message = serializers.ReadOnlyField()
    post_image = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'sender', 'notification_type', 'message', 'post', 'post_image', 'is_read', 'created_at']

    def get_post_image(self, obj):
        if obj.post:
            return obj.post.image_display_url
        return None