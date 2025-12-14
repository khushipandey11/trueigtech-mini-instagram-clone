import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Bell, CheckCheck } from "lucide-react";
import axios from "axios";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    loadNotifications();
  }, []);

  const loadNotifications = async () => {
    try {
      const response = await axios.get("/notifications/");
      setNotifications(response.data);
    } catch (error) {
      console.error("Error loading notifications:", error);
    }
    setLoading(false);
  };

  const markAsRead = async (notificationId) => {
    try {
      await axios.post(`/notifications/${notificationId}/read/`);
      setNotifications(
        notifications.map((n) =>
          n.id === notificationId ? { ...n, is_read: true } : n
        )
      );
    } catch (error) {
      console.error("Error marking notification as read:", error);
    }
  };

  const markAllAsRead = async () => {
    try {
      await axios.post("/notifications/read-all/");
      setNotifications(notifications.map((n) => ({ ...n, is_read: true })));
    } catch (error) {
      console.error("Error marking all notifications as read:", error);
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

  if (loading) {
    return (
      <div className="text-center p-3">
        <div className="loading-spinner"></div>
        <p>Loading notifications...</p>
      </div>
    );
  }

  return (
    <div>
      <div className="card">
        <div
          style={{
            padding: "20px",
            borderBottom: "1px solid var(--border-light)",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <h3>Notifications</h3>
          {notifications.some((n) => !n.is_read) && (
            <button
              className="btn btn-secondary"
              onClick={markAllAsRead}
              style={{ padding: "6px 12px", fontSize: "12px" }}
            >
              <CheckCheck size={16} style={{ marginRight: "4px" }} />
              Mark All Read
            </button>
          )}
        </div>

        {notifications.length === 0 ? (
          <div className="text-center p-3">
            <Bell
              size={48}
              style={{ color: "var(--text-secondary)", marginBottom: "16px" }}
            />
            <h3 style={{ marginBottom: "8px" }}>No notifications yet</h3>
            <p className="text-secondary">
              When someone likes your posts, comments, or follows you, you'll
              see it here
            </p>
          </div>
        ) : (
          <div>
            {notifications.map((notification) => (
              <div
                key={notification.id}
                className={`notification-item ${
                  !notification.is_read ? "unread" : ""
                }`}
                onClick={() => {
                  if (!notification.is_read) {
                    markAsRead(notification.id);
                  }
                  if (notification.post) {
                    navigate("/");
                  } else if (notification.notification_type === "follow") {
                    navigate(`/profile/${notification.sender.id}`);
                  }
                }}
              >
                {notification.sender.profile?.profile_picture_url ? (
                  <img
                    src={notification.sender.profile.profile_picture_url}
                    alt="Profile"
                    style={{
                      width: "40px",
                      height: "40px",
                      borderRadius: "50%",
                      objectFit: "cover",
                      marginRight: "12px",
                    }}
                  />
                ) : (
                  <div className="user-avatar" style={{ marginRight: "12px" }}>
                    {notification.sender.username.charAt(0).toUpperCase()}
                  </div>
                )}

                <div style={{ flex: 1 }}>
                  <p style={{ margin: 0, fontSize: "14px", lineHeight: "1.4" }}>
                    {notification.message}
                  </p>
                  <p
                    style={{
                      margin: 0,
                      color: "var(--text-secondary)",
                      fontSize: "12px",
                      marginTop: "4px",
                    }}
                  >
                    {formatTime(notification.created_at)}
                  </p>
                </div>

                {notification.post_image && (
                  <img
                    src={notification.post_image}
                    alt="Post"
                    style={{
                      width: "44px",
                      height: "44px",
                      objectFit: "cover",
                      borderRadius: "8px",
                      marginLeft: "12px",
                    }}
                  />
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Notifications;
