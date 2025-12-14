from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Post, Like, Comment, Follow, Notification, UserProfile, Story
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserSerializer,
    PostSerializer, PostCreateSerializer, CommentSerializer, 
    FollowSerializer, NotificationSerializer, UserProfileSerializer,
    StorySerializer, StoryCreateSerializer
)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            return get_object_or_404(User, id=user_id)
        return self.request.user

class ProfilePictureUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return User.objects.filter(
                username__icontains=query
            ).exclude(id=self.request.user.id)[:10]
        return User.objects.none()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    
    if user_to_follow == request.user:
        return Response({'error': 'Cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )
    
    if created:
        Notification.objects.get_or_create(
            recipient=user_to_follow,
            sender=request.user,
            notification_type='follow'
        )
        return Response({'message': 'Successfully followed user', 'following': True}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Already following this user', 'following': True}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    
    try:
        follow = Follow.objects.get(follower=request.user, following=user_to_unfollow)
        follow.delete()
        return Response({'message': 'Successfully unfollowed user', 'following': False}, status=status.HTTP_200_OK)
    except Follow.DoesNotExist:
        return Response({'error': 'Not following this user', 'following': False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def check_follow_status(request, user_id):
    user_to_check = get_object_or_404(User, id=user_id)
    is_following = Follow.objects.filter(follower=request.user, following=user_to_check).exists()
    return Response({'following': is_following})

class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = self.request.user
        
        follower_ids = Follow.objects.filter(following=user).values_list('follower', flat=True)
        return User.objects.filter(id__in=follower_ids)

class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = self.request.user
        
        following_ids = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return User.objects.filter(id__in=following_ids)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(user=request.user)
        return Response(PostSerializer(post, context={'request': request}).data, status=status.HTTP_201_CREATED)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return Post.objects.filter(user__in=list(following_users) + [user.id])

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = self.request.user
        return Post.objects.filter(user=user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        if post.user != request.user:
            Notification.objects.get_or_create(
                recipient=post.user,
                sender=request.user,
                notification_type='like',
                post=post
            )
        return Response({'message': 'Post liked', 'liked': True}, status=status.HTTP_201_CREATED)
    else:
        like.delete()
        if post.user != request.user:
            Notification.objects.filter(
                recipient=post.user,
                sender=request.user,
                notification_type='like',
                post=post
            ).delete()
        return Response({'message': 'Post unliked', 'liked': False}, status=status.HTTP_200_OK)

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        comment = serializer.save(user=self.request.user, post=post)
        
        if post.user != self.request.user:
            Notification.objects.get_or_create(
                recipient=post.user,
                sender=self.request.user,
                notification_type='comment',
                post=post
            )

class StoryListCreateView(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return Story.objects.filter(
            user__in=list(following_users) + [user.id],
            expires_at__gt=timezone.now()
        ).order_by('-created_at')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StoryCreateSerializer
        return StorySerializer

    def perform_create(self, serializer):
        expires_at = timezone.now() + timedelta(hours=24)
        serializer.save(user=self.request.user, expires_at=expires_at)

class UserStoriesView(generics.ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = self.request.user
        return Story.objects.filter(user=user, expires_at__gt=timezone.now())

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_notification_read(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification marked as read'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_all_notifications_read(request):
    Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
    return Response({'message': 'All notifications marked as read'})