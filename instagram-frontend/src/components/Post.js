import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Heart, MessageCircle, Send } from "lucide-react";
import { useAuth } from "../contexts/AuthContext";

const Post = ({
  post,
  onLike,
  onComment,
  onFollow,
  onUnfollow,
  showFollowButton = false,
}) => {
  const [commentText, setCommentText] = useState("");
  const [showComments, setShowComments] = useState(false);
  const [submittingComment, setSubmittingComment] = useState(false);
  const { user } = useAuth();
  const navigate = useNavigate();

  const isOwnPost = user && post.user.id === user.id;

  const handleLike = () => {
    onLike(post.id);
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    if (!commentText.trim()) return;

    setSubmittingComment(true);
    try {
      await onComment(post.id, commentText.trim());
      setCommentText("");
    } catch (error) {
      console.error("Error submitting comment:", error);
    }
    setSubmittingComment(false);
  };

  const handleFollow = () => {
    if (post.user.is_following) {
      onUnfollow(post.user.id);
    } else {
      onFollow(post.user.id);
    }
  };

  const formatTime = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffInSeconds = Math.floor((now - date) / 1000);

    if (diffInSeconds < 60) return "Just now";
    if (diffInSeconds < 3600) return `${Math.floor(diffInSeconds / 60)}m ago`;
    if (diffInSeconds < 86400)
      return `${Math.floor(diffInSeconds / 3600)}h ago`;
    return `${Math.floor(diffInSeconds / 86400)}d ago`;
  };

  return (
    <article className="post">
      <div className="post-header">
        <div
          className="post-user"
          onClick={() => navigate(`/profile/${post.user.id}`)}
        >
          {post.user.profile?.profile_picture_url ? (
            <img
              src={post.user.profile.profile_picture_url}
              alt="Profile"
              style={{
                width: "44px",
                height: "44px",
                borderRadius: "50%",
                objectFit: "cover",
                marginRight: "16px",
              }}
            />
          ) : (
            <div className="user-avatar">
              {post.user.username.charAt(0).toUpperCase()}
            </div>
          )}
          <div>
            <div className="username">{post.user.username}</div>
            <div className="text-secondary" style={{ fontSize: "12px" }}>
              {formatTime(post.created_at)}
            </div>
          </div>
        </div>

        {showFollowButton && !isOwnPost && (
          <button
            className={`btn ${
              post.user.is_following ? "btn-secondary" : "btn-primary"
            }`}
            onClick={handleFollow}
            style={{ padding: "6px 16px", fontSize: "12px" }}
          >
            {post.user.is_following ? "Following" : "Follow"}
          </button>
        )}
      </div>

      <img
        src={post.image_display_url || post.image_url}
        alt="Post"
        className="post-image"
        onError={(e) => {
          e.target.src =
            "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxOCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkltYWdlIG5vdCBmb3VuZDwvdGV4dD48L3N2Zz4=";
        }}
      />

      <div className="post-actions">
        <button
          className="action-btn"
          onClick={handleLike}
          style={{
            color: post.is_liked ? "var(--error-color)" : "var(--text-primary)",
          }}
        >
          <Heart size={20} fill={post.is_liked ? "currentColor" : "none"} />
          <span>{post.likes_count}</span>
        </button>

        <button
          className="action-btn"
          onClick={() => setShowComments(!showComments)}
        >
          <MessageCircle size={20} />
          <span>{post.comments_count}</span>
        </button>

        <button
          className="action-btn"
          onClick={() =>
            document.getElementById(`comment-input-${post.id}`)?.focus()
          }
        >
          <Send size={20} />
          <span>Comment</span>
        </button>
      </div>

      {post.caption && (
        <div className="post-caption">
          <span className="username">{post.user.username}</span> {post.caption}
        </div>
      )}

      <div className="post-comments">
        {post.comments.slice(0, 2).map((comment) => (
          <div key={comment.id} className="comment">
            <span className="comment-user">{comment.user.username}</span>
            {comment.text}
          </div>
        ))}

        {post.comments_count > 2 && !showComments && (
          <button
            onClick={() => setShowComments(true)}
            style={{
              background: "none",
              border: "none",
              color: "var(--text-secondary)",
              cursor: "pointer",
              fontSize: "14px",
              padding: "4px 0",
            }}
          >
            View all {post.comments_count} comments
          </button>
        )}
      </div>

      {showComments && post.comments.length > 2 && (
        <div
          style={{
            maxHeight: "300px",
            overflowY: "auto",
            padding: "0 20px",
          }}
        >
          {post.comments.slice(2).map((comment) => (
            <div
              key={comment.id}
              className="comment"
              style={{
                padding: "8px 0",
                borderBottom: "1px solid var(--border-light)",
              }}
            >
              <div>
                <span className="comment-user">{comment.user.username}</span>
                <span style={{ marginLeft: "8px" }}>{comment.text}</span>
              </div>
              <div
                className="text-secondary"
                style={{ fontSize: "12px", marginTop: "4px" }}
              >
                {formatTime(comment.created_at)}
              </div>
            </div>
          ))}
        </div>
      )}

      <form onSubmit={handleCommentSubmit} className="comment-form">
        <input
          id={`comment-input-${post.id}`}
          type="text"
          placeholder="Add a comment..."
          value={commentText}
          onChange={(e) => setCommentText(e.target.value)}
          className="comment-input"
          maxLength={500}
        />
        <button
          type="submit"
          className="comment-submit"
          disabled={!commentText.trim() || submittingComment}
        >
          {submittingComment ? "Posting..." : "Post"}
        </button>
      </form>
    </article>
  );
};

export default Post;
