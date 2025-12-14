import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Post from "./Post";
import axios from "axios";

const Feed = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [feedType, setFeedType] = useState("following");
  const navigate = useNavigate();

  const loadFeed = useCallback(async () => {
    setLoading(true);
    try {
      const endpoint = feedType === "following" ? "/feed/" : "/posts/";
      const response = await axios.get(endpoint);
      setPosts(response.data);
    } catch (error) {
      console.error("Error loading feed:", error);
    }
    setLoading(false);
  }, [feedType]);

  useEffect(() => {
    loadFeed();
  }, [loadFeed]);

  const handleLike = async (postId) => {
    try {
      await axios.post(`/posts/${postId}/like/`);
      loadFeed();
    } catch (error) {
      console.error("Error toggling like:", error);
    }
  };

  const handleComment = async (postId, text) => {
    try {
      await axios.post(`/posts/${postId}/comments/`, { text });
      loadFeed();
    } catch (error) {
      console.error("Error adding comment:", error);
      throw error;
    }
  };

  const handleFollow = async (userId) => {
    try {
      await axios.post(`/follow/${userId}/`);
      loadFeed();
    } catch (error) {
      console.error("Error following user:", error);
    }
  };

  const handleUnfollow = async (userId) => {
    try {
      await axios.delete(`/unfollow/${userId}/`);
      loadFeed();
    } catch (error) {
      console.error("Error unfollowing user:", error);
    }
  };

  if (loading) {
    return (
      <div className="text-center p-3">
        <div className="loading-spinner"></div>
        <p>Loading feed...</p>
      </div>
    );
  }

  return (
    <div>
      <div className="feed-tabs">
        <button
          className={`feed-tab ${feedType === "following" ? "active" : ""}`}
          onClick={() => setFeedType("following")}
        >
          Following
        </button>
        <button
          className={`feed-tab ${feedType === "explore" ? "active" : ""}`}
          onClick={() => setFeedType("explore")}
        >
          Explore
        </button>
      </div>

      {posts.length === 0 ? (
        <div className="card p-3 text-center">
          <div style={{ fontSize: "48px", marginBottom: "16px" }}>
            {feedType === "following" ? "👥" : "🌟"}
          </div>
          <h3 style={{ marginBottom: "12px" }}>No posts yet!</h3>
          <p
            className="text-secondary"
            style={{ marginBottom: "24px", lineHeight: "1.5" }}
          >
            {feedType === "following"
              ? "No posts from people you follow yet! Try exploring or following some users."
              : "No posts available yet!"}
          </p>
          <button
            className="btn btn-primary"
            onClick={() => navigate("/create")}
          >
            ✨ Create Your First Post
          </button>
        </div>
      ) : (
        posts.map((post) => (
          <Post
            key={post.id}
            post={post}
            onLike={handleLike}
            onComment={handleComment}
            onFollow={handleFollow}
            onUnfollow={handleUnfollow}
            showFollowButton={feedType === "explore"}
          />
        ))
      )}
    </div>
  );
};

export default Feed;
