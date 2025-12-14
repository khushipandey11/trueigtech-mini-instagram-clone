from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    
    path('profile/', views.ProfileView.as_view(), name='my-profile'),
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='user-profile'),
    path('profile/picture/', views.ProfilePictureUpdateView.as_view(), name='update-profile-picture'),
    
    path('users/search/', views.UserSearchView.as_view(), name='user-search'),
    
    path('follow/<int:user_id>/', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
    path('follow-status/<int:user_id>/', views.check_follow_status, name='follow-status'),
    
    path('posts/', views.PostListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('posts/user/<int:user_id>/', views.UserPostsView.as_view(), name='user-posts'),
    path('posts/my/', views.UserPostsView.as_view(), name='my-posts'),
    
    path('posts/<int:post_id>/like/', views.toggle_like, name='toggle-like'),
    
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='post-comments'),
    
    path('stories/', views.StoryListCreateView.as_view(), name='stories'),
    path('stories/user/<int:user_id>/', views.UserStoriesView.as_view(), name='user-stories'),
    path('stories/my/', views.UserStoriesView.as_view(), name='my-stories'),
    
    path('followers/', views.FollowersListView.as_view(), name='my-followers'),
    path('followers/<int:user_id>/', views.FollowersListView.as_view(), name='user-followers'),
    path('following/', views.FollowingListView.as_view(), name='my-following'),
    path('following/<int:user_id>/', views.FollowingListView.as_view(), name='user-following'),
    
    path('notifications/', views.NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark-notification-read'),
    path('notifications/read-all/', views.mark_all_notifications_read, name='mark-all-notifications-read'),
]