from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse

def frontend_app(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Clone</title>
    <style>
        :root {
            /* Light theme variables */
            --bg-primary: #fafafa;
            --bg-secondary: #ffffff;
            --bg-tertiary: #f8f9fa;
            --text-primary: #262626;
            --text-secondary: #8e8e8e;
            --border-color: #dbdbdb;
            --border-light: #efefef;
            --accent-color: #0095f6;
            --accent-hover: #0077cc;
            --error-color: #ed4956;
            --success-color: #00c851;
            --shadow: 0 2px 10px rgba(0,0,0,0.1);
            --shadow-hover: 0 4px 20px rgba(0,0,0,0.15);
        }

        [data-theme="dark"] {
            /* Dark theme variables */
            --bg-primary: #000000;
            --bg-secondary: #1a1a1a;
            --bg-tertiary: #262626;
            --text-primary: #ffffff;
            --text-secondary: #a8a8a8;
            --border-color: #363636;
            --border-light: #2a2a2a;
            --accent-color: #0095f6;
            --accent-hover: #1ba1f2;
            --error-color: #ed4956;
            --success-color: #00c851;
            --shadow: 0 2px 10px rgba(0,0,0,0.3);
            --shadow-hover: 0 4px 20px rgba(0,0,0,0.4);
        }

        * { 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }
        
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            background: var(--bg-primary); 
            color: var(--text-primary);
            line-height: 1.6;
        }
        
        .header { 
            background: var(--bg-secondary); 
            border-bottom: 1px solid var(--border-color); 
            padding: 12px 0; 
            position: fixed; 
            top: 0; 
            width: 100%; 
            z-index: 100;
            backdrop-filter: blur(10px);
            box-shadow: var(--shadow);
        }
        
        .header-content { 
            max-width: 975px; 
            margin: 0 auto; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            padding: 0 20px; 
        }
        
        .logo { 
            font-size: 28px; 
            font-weight: bold; 
            background: linear-gradient(45deg, var(--accent-color), #e91e63);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .nav-buttons { 
            display: flex; 
            align-items: center; 
            gap: 8px; 
        }
        
        .nav-buttons button { 
            padding: 10px 16px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer; 
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s ease;
            position: relative;
        }
        
        .btn-primary { 
            background: var(--accent-color); 
            color: white; 
        }
        
        .btn-primary:hover { 
            background: var(--accent-hover); 
            transform: translateY(-1px);
        }
        
        .btn-secondary { 
            background: var(--bg-tertiary); 
            color: var(--text-primary); 
            border: 1px solid var(--border-color); 
        }
        
        .btn-secondary:hover { 
            background: var(--border-color); 
            transform: translateY(-1px);
        }
        
        .theme-toggle {
            background: none !important;
            border: none !important;
            font-size: 20px;
            padding: 8px !important;
            border-radius: 50% !important;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        
        .theme-toggle:hover {
            transform: scale(1.1) rotate(15deg);
        }
        
        .main { 
            margin-top: 80px; 
            max-width: 600px; 
            margin-left: auto; 
            margin-right: auto; 
            padding: 20px; 
        }
        
        .auth-form { 
            background: var(--bg-secondary); 
            padding: 40px; 
            border-radius: 16px; 
            box-shadow: var(--shadow); 
            margin-bottom: 20px;
            border: 1px solid var(--border-color);
        }
        
        .form-group { 
            margin-bottom: 20px; 
        }
        
        .form-group input, .form-group textarea { 
            width: 100%; 
            padding: 14px; 
            border: 2px solid var(--border-color); 
            border-radius: 8px; 
            font-size: 14px;
            background: var(--bg-secondary);
            color: var(--text-primary);
            transition: border-color 0.2s ease;
        }
        
        .form-group input:focus, .form-group textarea:focus { 
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(0, 149, 246, 0.1);
        }
        
        .form-group button { 
            width: 100%; 
            padding: 14px; 
            background: var(--accent-color); 
            color: white; 
            border: none; 
            border-radius: 8px; 
            font-size: 14px; 
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .form-group button:hover { 
            background: var(--accent-hover);
            transform: translateY(-1px);
        }
        
        .post { 
            background: var(--bg-secondary); 
            border-radius: 16px; 
            margin-bottom: 24px; 
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            overflow: hidden;
            transition: box-shadow 0.3s ease;
        }
        
        .post:hover {
            box-shadow: var(--shadow-hover);
        }
        
        .post-header { 
            padding: 16px 20px; 
            display: flex; 
            align-items: center; 
            border-bottom: 1px solid var(--border-light); 
        }
        
        .post-user { 
            font-weight: 600; 
            margin-left: 12px;
            cursor: pointer;
            transition: color 0.2s ease;
        }
        
        .post-user:hover {
            color: var(--accent-color);
        }
        
        .post-image { 
            width: 100%; 
            max-height: 600px; 
            object-fit: cover; 
            display: block;
        }
        
        .post-actions { 
            padding: 16px 20px; 
            display: flex;
            gap: 16px;
        }
        
        .post-actions button { 
            background: none; 
            border: none; 
            font-size: 16px; 
            cursor: pointer;
            color: var(--text-primary);
            transition: all 0.2s ease;
            padding: 8px;
            border-radius: 8px;
        }
        
        .post-actions button:hover {
            background: var(--bg-tertiary);
            transform: scale(1.05);
        }
        
        .post-caption { 
            padding: 0 20px 16px; 
            line-height: 1.5;
        }
        
        .post-comments { 
            padding: 0 20px 16px; 
        }
        
        .comment { 
            margin-bottom: 8px; 
            line-height: 1.4;
        }
        
        .comment-user { 
            font-weight: 600; 
            margin-right: 8px; 
        }
        
        .profile-header { 
            background: var(--bg-secondary); 
            padding: 40px; 
            border-radius: 16px; 
            margin-bottom: 24px; 
            text-align: center;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }
        
        .profile-stats { 
            display: flex; 
            justify-content: center; 
            gap: 40px; 
            margin: 24px 0; 
        }
        
        .stat { 
            text-align: center;
            cursor: pointer;
            padding: 12px;
            border-radius: 8px;
            transition: background 0.2s ease;
        }
        
        .stat:hover {
            background: var(--bg-tertiary);
        }
        
        .stat-number { 
            font-weight: bold; 
            font-size: 20px; 
        }
        
        .stat-label { 
            color: var(--text-secondary); 
            font-size: 14px; 
        }
        
        .hidden { display: none; }
        .error { color: var(--error-color); font-size: 14px; margin-top: 8px; }
        .success { color: var(--success-color); font-size: 14px; margin-top: 8px; }
        
        .posts-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); 
            gap: 16px; 
        }
        
        .post-thumbnail { 
            aspect-ratio: 1; 
            background-size: cover; 
            background-position: center; 
            border-radius: 12px; 
            cursor: pointer;
            transition: transform 0.2s ease;
            border: 1px solid var(--border-color);
        }
        
        .post-thumbnail:hover {
            transform: scale(1.02);
        }
        
        .search-container { 
            background: var(--bg-secondary); 
            padding: 24px; 
            border-radius: 16px; 
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }
        
        .search-input { 
            width: 100%; 
            padding: 14px; 
            border: 2px solid var(--border-color); 
            border-radius: 12px; 
            font-size: 14px;
            background: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .search-input:focus {
            outline: none;
            border-color: var(--accent-color);
        }
        
        .user-result { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            padding: 16px; 
            border-bottom: 1px solid var(--border-light);
            transition: background 0.2s ease;
        }
        
        .user-result:hover {
            background: var(--bg-tertiary);
        }
        
        .user-info { 
            display: flex; 
            align-items: center; 
        }
        
        .user-avatar { 
            width: 44px; 
            height: 44px; 
            border-radius: 50%; 
            background: linear-gradient(45deg, var(--accent-color), #e91e63); 
            color: white; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-weight: bold; 
            margin-right: 16px; 
        }
        
        .user-details h4 { 
            margin: 0; 
            font-size: 15px; 
            font-weight: 600;
        }
        
        .user-details p { 
            margin: 0; 
            color: var(--text-secondary); 
            font-size: 13px; 
        }
        
        .follow-btn { 
            padding: 8px 20px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer; 
            font-size: 13px;
            font-weight: 600;
            transition: all 0.2s ease;
        }
        
        .follow-btn.following { 
            background: var(--bg-tertiary); 
            color: var(--text-primary); 
            border: 1px solid var(--border-color); 
        }
        
        .follow-btn.not-following { 
            background: var(--accent-color); 
            color: white; 
        }
        
        .follow-btn:hover {
            transform: translateY(-1px);
        }
        
        .feed-tabs { 
            display: flex; 
            justify-content: center; 
            margin-bottom: 24px;
            background: var(--bg-secondary);
            border-radius: 12px;
            padding: 4px;
            box-shadow: var(--shadow);
        }
        
        .feed-tabs button { 
            padding: 12px 24px; 
            border: none; 
            background: none; 
            cursor: pointer;
            border-radius: 8px;
            font-weight: 500;
            transition: all 0.2s ease;
            color: var(--text-secondary);
        }
        
        .feed-tabs button.active { 
            background: var(--accent-color);
            color: white;
        }
        
        .notification-badge { 
            position: absolute; 
            top: -2px; 
            right: -2px; 
            background: var(--error-color); 
            color: white; 
            border-radius: 50%; 
            padding: 2px 6px; 
            font-size: 10px; 
            min-width: 16px; 
            text-align: center;
            font-weight: bold;
        }
        
        .notification-item { 
            display: flex; 
            align-items: center; 
            padding: 16px; 
            border-bottom: 1px solid var(--border-light); 
            background: var(--bg-secondary);
            transition: background 0.2s ease;
            cursor: pointer;
        }
        
        .notification-item:hover {
            background: var(--bg-tertiary);
        }
        
        .notification-item.unread { 
            background: var(--bg-tertiary); 
            border-left: 3px solid var(--accent-color);
        }
        
        .notification-avatar { 
            width: 44px; 
            height: 44px; 
            border-radius: 50%; 
            background: linear-gradient(45deg, var(--accent-color), #e91e63); 
            color: white; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-weight: bold; 
            margin-right: 16px; 
        }
        
        .notification-content { 
            flex: 1; 
        }
        
        .notification-text { 
            margin: 0; 
            font-size: 14px; 
            line-height: 1.4;
        }
        
        .notification-time { 
            color: var(--text-secondary); 
            font-size: 12px; 
            margin-top: 4px; 
        }
        
        .notification-post-image { 
            width: 44px; 
            height: 44px; 
            object-fit: cover; 
            border-radius: 8px; 
            margin-left: 12px; 
        }
        
        .followers-container { 
            background: var(--bg-secondary); 
            border-radius: 16px; 
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
        }
        
        .followers-header { 
            padding: 24px; 
            border-bottom: 1px solid var(--border-light); 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
        }
        
        .followers-tabs { 
            display: flex;
            background: var(--bg-primary);
            border-radius: 8px;
            padding: 4px;
        }
        
        .followers-tabs button { 
            padding: 8px 16px; 
            border: none; 
            background: none; 
            cursor: pointer;
            border-radius: 6px;
            font-weight: 500;
            transition: all 0.2s ease;
            color: var(--text-secondary);
        }
        
        .followers-tabs button.active { 
            background: var(--accent-color);
            color: white;
        }
        
        .comment-form { 
            padding: 16px 20px; 
            border-top: 1px solid var(--border-light); 
            display: flex; 
            gap: 12px; 
            align-items: center; 
        }
        
        .comment-input { 
            flex: 1; 
            padding: 10px 16px; 
            border: 1px solid var(--border-color); 
            border-radius: 20px; 
            font-size: 14px; 
            outline: none; 
            resize: none;
            background: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .comment-input:focus { 
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(0, 149, 246, 0.1);
        }
        
        .comment-submit { 
            padding: 10px 20px; 
            background: var(--accent-color); 
            color: white; 
            border: none; 
            border-radius: 20px; 
            cursor: pointer; 
            font-size: 14px; 
            font-weight: 600;
            transition: all 0.2s ease; 
        }
        
        .comment-submit:hover { 
            background: var(--accent-hover);
            transform: translateY(-1px);
        }
        
        .comment-submit:disabled { 
            background: var(--text-secondary); 
            cursor: not-allowed;
            transform: none;
        }
        
        .comments-section { 
            max-height: 300px; 
            overflow-y: auto; 
        }
        
        .comment-expanded { 
            padding: 12px 20px;
            border-bottom: 1px solid var(--border-light);
        }
        
        .show-comments-btn { 
            background: none; 
            border: none; 
            color: var(--text-secondary); 
            font-size: 14px; 
            cursor: pointer; 
            padding: 8px 20px 12px;
            transition: color 0.2s ease;
        }
        
        .show-comments-btn:hover { 
            color: var(--text-primary); 
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .main { padding: 16px; }
            .header-content { padding: 0 16px; }
            .logo { font-size: 24px; }
            .nav-buttons button { padding: 8px 12px; font-size: 13px; }
            .profile-stats { gap: 20px; }
            .posts-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; }
        }

        /* Smooth scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: var(--bg-primary); }
        ::-webkit-scrollbar-thumb { background: var(--border-color); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }

        /* Loading animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .post {
            animation: fadeIn 0.5s ease-out;
        }

        .notification-badge {
            animation: pulse 2s infinite;
        }

        .user-avatar {
            transition: transform 0.2s ease;
        }

        .user-avatar:hover {
            transform: scale(1.1);
        }

        /* Focus styles for accessibility */
        button:focus, input:focus, textarea:focus {
            outline: 2px solid var(--accent-color);
            outline-offset: 2px;
        }

        /* Loading state */
        .loading {
            opacity: 0.6;
            pointer-events: none;
        }

        .loading::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            margin: -10px 0 0 -10px;
            border: 2px solid var(--accent-color);
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Enhanced hover effects */
        .post-actions button:active {
            transform: scale(0.95);
        }

        .btn-primary:active, .btn-secondary:active {
            transform: translateY(0);
        }

        /* Better form styling */
        .form-group input::placeholder, .form-group textarea::placeholder {
            color: var(--text-secondary);
        }

        /* Improved notification styling */
        .notification-item {
            position: relative;
        }

        .notification-item.unread::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: var(--accent-color);
        }

        /* Better mobile experience */
        @media (max-width: 480px) {
            .header-content {
                padding: 0 12px;
            }
            
            .main {
                padding: 12px;
            }
            
            .auth-form {
                padding: 24px;
            }
            
            .post-header, .post-actions, .post-caption, .post-comments {
                padding-left: 16px;
                padding-right: 16px;
            }
            
            .comment-form {
                padding: 12px 16px;
            }
            
            .profile-stats {
                gap: 16px;
            }
            
            .nav-buttons button {
                padding: 6px 10px;
                font-size: 12px;
            }
            
            .logo {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo">📸 Instagram</div>
            <div class="nav-buttons">
                <button id="themeToggle" class="theme-toggle" title="Toggle theme">🌙</button>
                <button id="homeBtn" class="btn-secondary hidden">Home</button>
                <button id="searchBtn" class="btn-secondary hidden">Search</button>
                <button id="notificationsBtn" class="btn-secondary hidden">
                    <span id="notificationIcon">🔔</span>
                    <span id="notificationBadge" class="notification-badge hidden">0</span>
                </button>
                <button id="profileBtn" class="btn-secondary hidden">Profile</button>
                <button id="createBtn" class="btn-secondary hidden">Create</button>
                <button id="logoutBtn" class="btn-secondary hidden">Logout</button>
            </div>
        </div>
    </div>

    <div class="main">
        <!-- Auth Forms -->
        <div id="authSection">
            <div class="auth-form">
                <h2 id="authTitle">Login</h2>
                <form id="authForm">
                    <div class="form-group">
                        <input type="text" id="username" placeholder="Username" required>
                    </div>
                    <div class="form-group">
                        <input type="password" id="password" placeholder="Password" required>
                    </div>
                    <div class="form-group hidden" id="emailGroup">
                        <input type="email" id="email" placeholder="Email">
                    </div>
                    <div class="form-group hidden" id="nameGroup">
                        <input type="text" id="firstName" placeholder="First Name">
                        <input type="text" id="lastName" placeholder="Last Name" style="margin-top: 10px;">
                    </div>
                    <div class="form-group hidden" id="confirmGroup">
                        <input type="password" id="passwordConfirm" placeholder="Confirm Password">
                    </div>
                    <div class="form-group">
                        <button type="submit" id="authSubmit">Login</button>
                    </div>
                    <div id="authError" class="error hidden"></div>
                </form>
                <p style="text-align: center; margin-top: 20px;">
                    <span id="authToggleText">Don't have an account?</span>
                    <a href="#" id="authToggle" style="color: #0095f6;">Sign up</a>
                </p>
            </div>
        </div>

        <!-- Feed Section -->
        <div id="feedSection" class="hidden">
            <div class="feed-tabs">
                <button id="followingTab" class="active" onclick="showFollowingFeed()">Following</button>
                <button id="exploreTab" onclick="showExploreFeed()">Explore</button>
            </div>
            <div id="feedPosts"></div>
        </div>

        <!-- Search Section -->
        <div id="searchSection" class="hidden">
            <div class="search-container">
                <input type="text" id="searchInput" class="search-input" placeholder="Search users..." onkeyup="searchUsers()">
                <div id="searchResults"></div>
            </div>
        </div>

        <!-- Notifications Section -->
        <div id="notificationsSection" class="hidden">
            <div class="followers-container">
                <div class="followers-header">
                    <h3>Notifications</h3>
                    <button onclick="markAllNotificationsRead()" class="btn-secondary">Mark All Read</button>
                </div>
                <div id="notificationsList"></div>
            </div>
        </div>

        <!-- Followers/Following Section -->
        <div id="followersSection" class="hidden">
            <div class="followers-container">
                <div class="followers-header">
                    <h3 id="followersTitle">Followers & Following</h3>
                </div>
                <div class="followers-tabs">
                    <button id="followersTab" class="active" onclick="showFollowersTab()">Followers</button>
                    <button id="followingTab" onclick="showFollowingTab()">Following</button>
                </div>
                <div id="followersContent"></div>
            </div>
        </div>

        <!-- Profile Section -->
        <div id="profileSection" class="hidden">
            <div class="profile-header">
                <h2 id="profileUsername"></h2>
                <div class="profile-stats">
                    <div class="stat">
                        <div class="stat-number" id="postsCount">0</div>
                        <div class="stat-label">posts</div>
                    </div>
                    <div class="stat" onclick="showFollowersModal('followers')" style="cursor: pointer;">
                        <div class="stat-number" id="followersCount">0</div>
                        <div class="stat-label">followers</div>
                    </div>
                    <div class="stat" onclick="showFollowersModal('following')" style="cursor: pointer;">
                        <div class="stat-number" id="followingCount">0</div>
                        <div class="stat-label">following</div>
                    </div>
                </div>
                <button id="followBtn" class="btn-primary hidden">Follow</button>
            </div>
            <div id="profilePosts" class="posts-grid"></div>
        </div>

        <!-- Create Post Section -->
        <div id="createSection" class="hidden">
            <div class="auth-form">
                <h2>Create New Post</h2>
                <form id="createForm">
                    <div class="form-group">
                        <input type="url" id="imageUrl" placeholder="Image URL" required>
                    </div>
                    <div class="form-group">
                        <textarea id="caption" placeholder="Write a caption..." rows="3"></textarea>
                    </div>
                    <div class="form-group">
                        <button type="submit">Share Post</button>
                    </div>
                    <div id="createError" class="error hidden"></div>
                    <div id="createSuccess" class="success hidden"></div>
                </form>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = '/api';
        let currentUser = null;
        let authToken = localStorage.getItem('authToken');
        
        // Theme management
        const themeToggle = document.getElementById('themeToggle');
        const currentTheme = localStorage.getItem('theme') || 'light';
        
        // Set initial theme
        document.documentElement.setAttribute('data-theme', currentTheme);
        updateThemeIcon(currentTheme);
        
        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
        
        function updateThemeIcon(theme) {
            themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
            themeToggle.title = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
        }

        // DOM Elements
        const authSection = document.getElementById('authSection');
        const feedSection = document.getElementById('feedSection');
        const searchSection = document.getElementById('searchSection');
        const notificationsSection = document.getElementById('notificationsSection');
        const followersSection = document.getElementById('followersSection');
        const profileSection = document.getElementById('profileSection');
        const createSection = document.getElementById('createSection');
        const navButtons = document.querySelectorAll('.nav-buttons button');
        
        let currentFeedType = 'following'; // 'following' or 'explore'
        let currentFollowersTab = 'followers'; // 'followers' or 'following'

        // Initialize app
        if (authToken) {
            getCurrentUser().then(() => {
                showFeed();
                loadNotificationCount();
                // Check for new notifications every 30 seconds
                setInterval(loadNotificationCount, 30000);
            }).catch(() => {
                // Token might be expired
                localStorage.removeItem('authToken');
                authToken = null;
                showAuth();
            });
        } else {
            showAuth();
        }

        // Get current user info
        async function getCurrentUser() {
            const response = await fetch(API_BASE + '/profile/', {
                headers: { 'Authorization': `Bearer ${authToken}` }
            });
            
            if (response.ok) {
                currentUser = await response.json();
                console.log('Current user:', currentUser.username);
            } else {
                throw new Error('Failed to get user info');
            }
        }

        // Auth functionality
        let isLogin = true;
        const authForm = document.getElementById('authForm');
        const authToggle = document.getElementById('authToggle');

        authToggle.addEventListener('click', (e) => {
            e.preventDefault();
            isLogin = !isLogin;
            updateAuthForm();
        });

        function updateAuthForm() {
            const title = document.getElementById('authTitle');
            const submit = document.getElementById('authSubmit');
            const toggleText = document.getElementById('authToggleText');
            const emailGroup = document.getElementById('emailGroup');
            const nameGroup = document.getElementById('nameGroup');
            const confirmGroup = document.getElementById('confirmGroup');

            if (isLogin) {
                title.textContent = 'Login';
                submit.textContent = 'Login';
                toggleText.textContent = "Don't have an account?";
                authToggle.textContent = 'Sign up';
                emailGroup.classList.add('hidden');
                nameGroup.classList.add('hidden');
                confirmGroup.classList.add('hidden');
            } else {
                title.textContent = 'Sign Up';
                submit.textContent = 'Sign Up';
                toggleText.textContent = 'Have an account?';
                authToggle.textContent = 'Log in';
                emailGroup.classList.remove('hidden');
                nameGroup.classList.remove('hidden');
                confirmGroup.classList.remove('hidden');
            }
        }

        authForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(authForm);
            const data = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value
            };

            if (!isLogin) {
                data.email = document.getElementById('email').value;
                data.first_name = document.getElementById('firstName').value;
                data.last_name = document.getElementById('lastName').value;
                data.password_confirm = document.getElementById('passwordConfirm').value;
            }

            try {
                const endpoint = isLogin ? '/auth/login/' : '/auth/register/';
                const response = await fetch(API_BASE + endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                
                if (response.ok) {
                    authToken = result.access;
                    currentUser = result.user;
                    localStorage.setItem('authToken', authToken);
                    showFeed();
                } else {
                    showError('authError', result.detail || 'Authentication failed');
                }
            } catch (error) {
                showError('authError', 'Network error');
            }
        });

        // Navigation
        document.getElementById('homeBtn').addEventListener('click', showFeed);
        document.getElementById('searchBtn').addEventListener('click', showSearch);
        document.getElementById('notificationsBtn').addEventListener('click', showNotifications);
        document.getElementById('profileBtn').addEventListener('click', () => showProfile());
        document.getElementById('createBtn').addEventListener('click', showCreate);
        document.getElementById('logoutBtn').addEventListener('click', logout);

        function showAuth() {
            hideAllSections();
            authSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.add('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
        }

        function showFeed() {
            hideAllSections();
            feedSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
            loadFeed();
        }

        function showProfile(userId = null) {
            hideAllSections();
            profileSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
            loadProfile(userId);
        }

        function showSearch() {
            hideAllSections();
            searchSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
            document.getElementById('searchInput').focus();
        }

        function showNotifications() {
            hideAllSections();
            notificationsSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
            loadNotifications();
        }

        function showCreate() {
            hideAllSections();
            createSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
        }

        function showFollowersModal(type) {
            currentFollowersTab = type;
            hideAllSections();
            followersSection.classList.remove('hidden');
            navButtons.forEach(btn => btn.classList.remove('hidden'));
            document.getElementById('themeToggle').classList.remove('hidden');
            
            if (type === 'followers') {
                showFollowersTab();
            } else {
                showFollowingTab();
            }
        }

        function hideAllSections() {
            [authSection, feedSection, searchSection, notificationsSection, followersSection, profileSection, createSection].forEach(section => {
                section.classList.add('hidden');
            });
        }

        function logout() {
            localStorage.removeItem('authToken');
            authToken = null;
            currentUser = null;
            showAuth();
        }

        // Feed functionality
        async function loadFeed() {
            if (currentFeedType === 'following') {
                await loadFollowingFeed();
            } else {
                await loadExploreFeed();
            }
        }

        async function showFollowingFeed() {
            currentFeedType = 'following';
            document.getElementById('followingTab').classList.add('active');
            document.getElementById('exploreTab').classList.remove('active');
            await loadFollowingFeed();
        }

        async function showExploreFeed() {
            currentFeedType = 'explore';
            document.getElementById('exploreTab').classList.add('active');
            document.getElementById('followingTab').classList.remove('active');
            await loadExploreFeed();
        }

        async function loadFollowingFeed() {
            try {
                const response = await fetch(API_BASE + '/feed/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const posts = await response.json();
                    console.log('Following feed loaded:', posts.length, 'posts');
                    displayPosts(posts);
                } else {
                    console.error('Failed to load following feed:', response.status);
                }
            } catch (error) {
                console.error('Network error:', error);
            }
        }

        async function loadExploreFeed() {
            try {
                const response = await fetch(API_BASE + '/posts/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const posts = await response.json();
                    console.log('Explore feed loaded:', posts.length, 'posts');
                    displayPosts(posts, true); // true = show follow buttons
                }
            } catch (error) {
                console.error('Error loading explore feed:', error);
            }
        }

        function displayPosts(posts, showFollowButtons = false) {
            const container = document.getElementById('feedPosts');
            container.innerHTML = '';

            if (posts.length === 0) {
                const message = currentFeedType === 'following' 
                    ? 'No posts from people you follow yet! Try exploring or following some users.'
                    : 'No posts available yet!';
                const emoji = currentFeedType === 'following' ? '👥' : '🌟';
                container.innerHTML = `
                    <div style="text-align: center; padding: 60px 20px; color: var(--text-secondary);">
                        <div style="font-size: 48px; margin-bottom: 16px;">${emoji}</div>
                        <h3 style="color: var(--text-primary); margin-bottom: 12px;">No posts yet!</h3>
                        <p style="margin-bottom: 24px; line-height: 1.5;">${message}</p>
                        <button onclick="showCreate()" class="btn-primary">✨ Create Your First Post</button>
                    </div>
                `;
                return;
            }

            posts.forEach(post => {
                const postElement = createPostElement(post, showFollowButtons);
                container.appendChild(postElement);
            });
        }

        function createPostElement(post, showFollowButton = false) {
            const div = document.createElement('div');
            div.className = 'post';
            
            const isOwnPost = currentUser && post.user.id === currentUser.id;
            const followButton = (showFollowButton && !isOwnPost) ? 
                `<button onclick="toggleFollow(${post.user.id})" class="follow-btn ${post.user.is_following ? 'following' : 'not-following'}" id="follow-btn-${post.user.id}">
                    ${post.user.is_following ? 'Following' : 'Follow'}
                </button>` : '';
            
            const hasMoreComments = post.comments_count > 2;
            const visibleComments = post.comments.slice(0, 2);
            
            div.innerHTML = `
                <div class="post-header">
                    <div style="display: flex; align-items: center; flex: 1;">
                        <strong class="post-user" onclick="showProfile(${post.user.id})" style="cursor: pointer;">${post.user.username}</strong>
                    </div>
                    ${followButton}
                </div>
                <img src="${post.image_url}" alt="Post" class="post-image" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxOCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkltYWdlIG5vdCBmb3VuZDwvdGV4dD48L3N2Zz4='">
                <div class="post-actions">
                    <button onclick="toggleLike(${post.id})" style="color: ${post.is_liked ? '#ed4956' : '#262626'}">
                        ${post.is_liked ? '❤️' : '🤍'} ${post.likes_count}
                    </button>
                    <button onclick="toggleComments(${post.id})" style="color: #262626">
                        💬 ${post.comments_count}
                    </button>
                    <button onclick="focusCommentInput(${post.id})" style="color: #262626; font-size: 14px;">
                        💭 Comment
                    </button>
                </div>
                <div class="post-caption">
                    <strong>${post.user.username}</strong> ${post.caption}
                </div>
                <div class="post-comments" id="comments-preview-${post.id}">
                    ${visibleComments.map(comment => 
                        `<div class="comment">
                            <span class="comment-user">${comment.user.username}</span>
                            ${comment.text}
                        </div>`
                    ).join('')}
                    ${hasMoreComments ? `<button class="show-comments-btn" onclick="toggleComments(${post.id})">View all ${post.comments_count} comments</button>` : ''}
                </div>
                <div class="comments-section hidden" id="comments-full-${post.id}">
                    <div id="comments-list-${post.id}"></div>
                </div>
                <div class="comment-form">
                    <input type="text" class="comment-input" id="comment-input-${post.id}" placeholder="Add a comment..." maxlength="500" onkeypress="handleCommentKeyPress(event, ${post.id})" oninput="updateCommentButton(${post.id})">
                    <button class="comment-submit" id="comment-btn-${post.id}" onclick="addComment(${post.id})" disabled>Post</button>
                </div>
            `;
            return div;
        }

        // Like functionality
        async function toggleLike(postId) {
            try {
                const response = await fetch(`${API_BASE}/posts/${postId}/like/`, {
                    method: 'POST',
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    loadFeed(); // Refresh current feed
                }
            } catch (error) {
                console.error('Error toggling like:', error);
            }
        }

        // Profile functionality
        async function loadProfile(userId = null) {
            try {
                const endpoint = userId ? `/profile/${userId}/` : '/profile/';
                const response = await fetch(API_BASE + endpoint, {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const user = await response.json();
                    displayProfile(user);
                    loadUserPosts(userId);
                }
            } catch (error) {
                console.error('Error loading profile:', error);
            }
        }

        function displayProfile(user) {
            document.getElementById('profileUsername').textContent = user.username;
            document.getElementById('postsCount').textContent = user.posts_count;
            document.getElementById('followersCount').textContent = user.followers_count;
            document.getElementById('followingCount').textContent = user.following_count;
        }

        async function loadUserPosts(userId = null) {
            try {
                const endpoint = userId ? `/posts/user/${userId}/` : '/posts/my/';
                const response = await fetch(API_BASE + endpoint, {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const posts = await response.json();
                    displayUserPosts(posts);
                }
            } catch (error) {
                console.error('Error loading user posts:', error);
            }
        }

        function displayUserPosts(posts) {
            const container = document.getElementById('profilePosts');
            container.innerHTML = '';

            posts.forEach(post => {
                const div = document.createElement('div');
                div.className = 'post-thumbnail';
                div.style.backgroundImage = `url(${post.image_url})`;
                div.onclick = () => showPostDetail(post.id);
                container.appendChild(div);
            });
        }

        // Create post functionality
        document.getElementById('createForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const data = {
                image_url: document.getElementById('imageUrl').value,
                caption: document.getElementById('caption').value
            };

            try {
                const response = await fetch(API_BASE + '/posts/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${authToken}`
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    showSuccess('createSuccess', 'Post created successfully!');
                    document.getElementById('createForm').reset();
                    // Immediately show feed and refresh it
                    showFeed();
                } else {
                    const error = await response.json();
                    showError('createError', error.detail || 'Failed to create post');
                }
            } catch (error) {
                showError('createError', 'Network error');
            }
        });

        // Utility functions
        function showError(elementId, message) {
            const element = document.getElementById(elementId);
            element.textContent = message;
            element.classList.remove('hidden');
            setTimeout(() => element.classList.add('hidden'), 5000);
        }

        function showSuccess(elementId, message) {
            const element = document.getElementById(elementId);
            element.textContent = message;
            element.classList.remove('hidden');
            setTimeout(() => element.classList.add('hidden'), 3000);
        }

        // Search functionality
        let searchTimeout;
        async function searchUsers() {
            const query = document.getElementById('searchInput').value.trim();
            
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(async () => {
                if (query.length < 2) {
                    document.getElementById('searchResults').innerHTML = '';
                    return;
                }

                try {
                    const response = await fetch(`${API_BASE}/users/search/?q=${encodeURIComponent(query)}`, {
                        headers: { 'Authorization': `Bearer ${authToken}` }
                    });
                    
                    if (response.ok) {
                        const users = await response.json();
                        displaySearchResults(users);
                    }
                } catch (error) {
                    console.error('Search error:', error);
                }
            }, 300);
        }

        function displaySearchResults(users) {
            const container = document.getElementById('searchResults');
            
            if (users.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #8e8e8e; padding: 20px;">No users found</p>';
                return;
            }

            container.innerHTML = users.map(user => `
                <div class="user-result">
                    <div class="user-info" onclick="showProfile(${user.id})" style="cursor: pointer;">
                        <div class="user-avatar">${user.username.charAt(0).toUpperCase()}</div>
                        <div class="user-details">
                            <h4>${user.username}</h4>
                            <p>${user.first_name} ${user.last_name}</p>
                        </div>
                    </div>
                    <button onclick="toggleFollow(${user.id})" class="follow-btn ${user.is_following ? 'following' : 'not-following'}" id="follow-btn-${user.id}">
                        ${user.is_following ? 'Following' : 'Follow'}
                    </button>
                </div>
            `).join('');
        }

        // Follow/Unfollow functionality
        async function toggleFollow(userId) {
            try {
                const button = document.getElementById(`follow-btn-${userId}`);
                const isFollowing = button.classList.contains('following');
                
                const endpoint = isFollowing ? `/unfollow/${userId}/` : `/follow/${userId}/`;
                const method = isFollowing ? 'DELETE' : 'POST';
                
                const response = await fetch(API_BASE + endpoint, {
                    method: method,
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const result = await response.json();
                    updateFollowButton(userId, result.following);
                }
            } catch (error) {
                console.error('Follow toggle error:', error);
            }
        }

        function updateFollowButton(userId, isFollowing) {
            const button = document.getElementById(`follow-btn-${userId}`);
            if (button) {
                if (isFollowing) {
                    button.classList.remove('not-following');
                    button.classList.add('following');
                    button.textContent = 'Following';
                } else {
                    button.classList.remove('following');
                    button.classList.add('not-following');
                    button.textContent = 'Follow';
                }
            }
        }

        // Notifications functionality
        async function loadNotifications() {
            try {
                const response = await fetch(API_BASE + '/notifications/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const notifications = await response.json();
                    displayNotifications(notifications);
                }
            } catch (error) {
                console.error('Error loading notifications:', error);
            }
        }

        async function loadNotificationCount() {
            try {
                const response = await fetch(API_BASE + '/notifications/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const notifications = await response.json();
                    const unreadCount = notifications.filter(n => !n.is_read).length;
                    updateNotificationBadge(unreadCount);
                }
            } catch (error) {
                console.error('Error loading notification count:', error);
            }
        }

        function updateNotificationBadge(count) {
            const badge = document.getElementById('notificationBadge');
            if (count > 0) {
                badge.textContent = count > 99 ? '99+' : count;
                badge.classList.remove('hidden');
            } else {
                badge.classList.add('hidden');
            }
        }

        function displayNotifications(notifications) {
            const container = document.getElementById('notificationsList');
            
            if (notifications.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #8e8e8e; padding: 40px;">No notifications yet</p>';
                return;
            }

            container.innerHTML = notifications.map(notification => `
                <div class="notification-item ${!notification.is_read ? 'unread' : ''}" onclick="markNotificationRead(${notification.id})">
                    <div class="notification-avatar">${notification.sender.username.charAt(0).toUpperCase()}</div>
                    <div class="notification-content">
                        <p class="notification-text">${notification.message}</p>
                        <p class="notification-time">${formatTime(notification.created_at)}</p>
                    </div>
                    ${notification.post_image ? `<img src="${notification.post_image}" class="notification-post-image" alt="Post">` : ''}
                </div>
            `).join('');
        }

        async function markNotificationRead(notificationId) {
            try {
                await fetch(`${API_BASE}/notifications/${notificationId}/read/`, {
                    method: 'POST',
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                loadNotifications();
                loadNotificationCount();
            } catch (error) {
                console.error('Error marking notification as read:', error);
            }
        }

        async function markAllNotificationsRead() {
            try {
                await fetch(API_BASE + '/notifications/read-all/', {
                    method: 'POST',
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                loadNotifications();
                loadNotificationCount();
            } catch (error) {
                console.error('Error marking all notifications as read:', error);
            }
        }

        // Followers/Following functionality
        async function showFollowersTab() {
            currentFollowersTab = 'followers';
            document.getElementById('followersTab').classList.add('active');
            document.getElementById('followingTab').classList.remove('active');
            await loadFollowers();
        }

        async function showFollowingTab() {
            currentFollowersTab = 'following';
            document.getElementById('followingTab').classList.add('active');
            document.getElementById('followersTab').classList.remove('active');
            await loadFollowing();
        }

        async function loadFollowers() {
            try {
                const response = await fetch(API_BASE + '/followers/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const followers = await response.json();
                    displayFollowersList(followers, 'followers');
                }
            } catch (error) {
                console.error('Error loading followers:', error);
            }
        }

        async function loadFollowing() {
            try {
                const response = await fetch(API_BASE + '/following/', {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const following = await response.json();
                    displayFollowersList(following, 'following');
                }
            } catch (error) {
                console.error('Error loading following:', error);
            }
        }

        function displayFollowersList(users, type) {
            const container = document.getElementById('followersContent');
            
            if (users.length === 0) {
                const message = type === 'followers' ? 'No followers yet' : 'Not following anyone yet';
                container.innerHTML = `<p style="text-align: center; color: #8e8e8e; padding: 40px;">${message}</p>`;
                return;
            }

            container.innerHTML = users.map(user => `
                <div class="user-result">
                    <div class="user-info" onclick="showProfile(${user.id})" style="cursor: pointer;">
                        <div class="user-avatar">${user.username.charAt(0).toUpperCase()}</div>
                        <div class="user-details">
                            <h4>${user.username}</h4>
                            <p>${user.first_name} ${user.last_name}</p>
                        </div>
                    </div>
                    <button onclick="toggleFollow(${user.id})" class="follow-btn ${user.is_following ? 'following' : 'not-following'}" id="follow-btn-${user.id}">
                        ${user.is_following ? 'Following' : 'Follow'}
                    </button>
                </div>
            `).join('');
        }

        // Comment functionality
        async function toggleComments(postId) {
            const commentsSection = document.getElementById(`comments-full-${postId}`);
            const isHidden = commentsSection.classList.contains('hidden');
            
            if (isHidden) {
                await loadComments(postId);
                commentsSection.classList.remove('hidden');
            } else {
                commentsSection.classList.add('hidden');
            }
        }

        async function loadComments(postId) {
            try {
                const response = await fetch(`${API_BASE}/posts/${postId}/comments/`, {
                    headers: { 'Authorization': `Bearer ${authToken}` }
                });
                
                if (response.ok) {
                    const comments = await response.json();
                    displayComments(postId, comments);
                }
            } catch (error) {
                console.error('Error loading comments:', error);
            }
        }

        function displayComments(postId, comments) {
            const container = document.getElementById(`comments-list-${postId}`);
            
            if (comments.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #8e8e8e; padding: 20px;">No comments yet</p>';
                return;
            }

            container.innerHTML = comments.map(comment => `
                <div class="comment-expanded">
                    <strong>${comment.user.username}</strong>
                    <span style="margin-left: 8px;">${comment.text}</span>
                    <div style="color: #8e8e8e; font-size: 12px; margin-top: 4px;">
                        ${formatTime(comment.created_at)}
                    </div>
                </div>
            `).join('');
        }

        async function addComment(postId) {
            const input = document.getElementById(`comment-input-${postId}`);
            const button = document.getElementById(`comment-btn-${postId}`);
            const text = input.value.trim();
            
            if (!text) return;
            
            // Show loading state
            const originalText = button.textContent;
            button.textContent = 'Posting...';
            button.disabled = true;
            
            try {
                const response = await fetch(`${API_BASE}/posts/${postId}/comments/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${authToken}`
                    },
                    body: JSON.stringify({ text: text })
                });
                
                if (response.ok) {
                    input.value = '';
                    updateCommentButton(postId);
                    
                    // Show success feedback
                    button.textContent = 'Posted!';
                    button.style.background = '#00c851';
                    setTimeout(() => {
                        button.textContent = originalText;
                        button.style.background = '#0095f6';
                    }, 1000);
                    
                    // Refresh the feed to show updated comment count
                    loadFeed();
                    // If comments are expanded, reload them
                    const commentsSection = document.getElementById(`comments-full-${postId}`);
                    if (!commentsSection.classList.contains('hidden')) {
                        await loadComments(postId);
                    }
                } else {
                    const error = await response.json();
                    showError('createError', 'Failed to add comment: ' + (error.detail || 'Unknown error'));
                    button.textContent = originalText;
                    button.disabled = false;
                }
            } catch (error) {
                console.error('Error adding comment:', error);
                showError('createError', 'Network error while adding comment');
                button.textContent = originalText;
                button.disabled = false;
            }
        }

        function handleCommentKeyPress(event, postId) {
            if (event.key === 'Enter') {
                event.preventDefault();
                addComment(postId);
            }
        }

        function focusCommentInput(postId) {
            const input = document.getElementById(`comment-input-${postId}`);
            input.focus();
        }

        function updateCommentButton(postId) {
            const input = document.getElementById(`comment-input-${postId}`);
            const button = document.getElementById(`comment-btn-${postId}`);
            const hasText = input.value.trim().length > 0;
            
            button.disabled = !hasText;
            button.style.opacity = hasText ? '1' : '0.5';
        }

        // Utility function to format time
        function formatTime(dateString) {
            const date = new Date(dateString);
            const now = new Date();
            const diffInSeconds = Math.floor((now - date) / 1000);
            
            if (diffInSeconds < 60) return 'Just now';
            if (diffInSeconds < 3600) return `${Math.floor(diffInSeconds / 60)}m ago`;
            if (diffInSeconds < 86400) return `${Math.floor(diffInSeconds / 3600)}h ago`;
            return `${Math.floor(diffInSeconds / 86400)}d ago`;
        }
    </script>
</body>
</html>
    ''')

urlpatterns = [
    path('', frontend_app, name='frontend-app'),
]