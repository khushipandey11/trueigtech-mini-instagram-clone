#!/usr/bin/env python3
"""
Simple test script for Instagram Clone API
Run this after starting the Django server to test basic functionality
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'

def test_api():
    print("🧪 Testing Instagram Clone API...")
    
    # Test 1: Register a new user
    print("\n1. Testing user registration...")
    import random
    username = f'testuser{random.randint(1000, 9999)}'
    register_data = {
        'username': username,
        'email': f'test{random.randint(100, 999)}@example.com',
        'password': 'testpass123',
        'password_confirm': 'testpass123',
        'first_name': 'Test',
        'last_name': 'User'
    }
    
    response = requests.post(f'{BASE_URL}/auth/register/', json=register_data)
    if response.status_code == 201:
        print("✅ User registration successful")
        user_data = response.json()
        token = user_data['access']
        print(f"   Token: {token[:20]}...")
    else:
        print(f"❌ Registration failed: {response.text}")
        return
    
    # Test 2: Login
    print("\n2. Testing user login...")
    login_data = {
        'username': username,
        'password': 'testpass123'
    }
    
    response = requests.post(f'{BASE_URL}/auth/login/', json=login_data)
    if response.status_code == 200:
        print("✅ Login successful")
        token = response.json()['access']
    else:
        print(f"❌ Login failed: {response.text}")
        return
    
    headers = {'Authorization': f'Bearer {token}'}
    
    # Test 3: Create a post
    print("\n3. Testing post creation...")
    post_data = {
        'image_url': 'https://picsum.photos/400/400',
        'caption': 'My first test post! 📸'
    }
    
    response = requests.post(f'{BASE_URL}/posts/', json=post_data, headers=headers)
    if response.status_code == 201:
        print("✅ Post creation successful")
        post = response.json()
        post_id = post['id']
        print(f"   Post ID: {post_id}")
    else:
        print(f"❌ Post creation failed: {response.text}")
        return
    
    # Test 4: Get feed
    print("\n4. Testing feed retrieval...")
    response = requests.get(f'{BASE_URL}/feed/', headers=headers)
    if response.status_code == 200:
        posts = response.json()
        print(f"✅ Feed retrieved successfully ({len(posts)} posts)")
    else:
        print(f"❌ Feed retrieval failed: {response.text}")
    
    # Test 5: Like a post
    print("\n5. Testing post like...")
    response = requests.post(f'{BASE_URL}/posts/{post_id}/like/', headers=headers)
    if response.status_code in [200, 201]:
        print("✅ Post like successful")
    else:
        print(f"❌ Post like failed: {response.text}")
    
    # Test 6: Comment on a post
    print("\n6. Testing post comment...")
    comment_data = {'text': 'Great post! 👍'}
    response = requests.post(f'{BASE_URL}/posts/{post_id}/comments/', json=comment_data, headers=headers)
    if response.status_code == 201:
        print("✅ Comment creation successful")
    else:
        print(f"❌ Comment creation failed: {response.text}")
    
    # Test 7: Get profile
    print("\n7. Testing profile retrieval...")
    response = requests.get(f'{BASE_URL}/profile/', headers=headers)
    if response.status_code == 200:
        profile = response.json()
        print(f"✅ Profile retrieved: {profile['username']} ({profile['posts_count']} posts)")
    else:
        print(f"❌ Profile retrieval failed: {response.text}")
    
    print("\n🎉 API testing completed!")
    print("\n📱 You can now:")
    print("   • Visit http://127.0.0.1:8000/ for the home page")
    print("   • Visit http://127.0.0.1:8000/app/ for the frontend app")
    print("   • Visit http://127.0.0.1:8000/admin/ for admin panel (admin/admin123)")

if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure Django server is running on http://127.0.0.1:8000/")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")