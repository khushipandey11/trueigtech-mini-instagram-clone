import React, { useState, useEffect, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Users, UserPlus, Grid, Camera } from "lucide-react";
import { useAuth } from "../contexts/AuthContext";
import axios from "axios";

const Profile = () => {
  const { userId } = useParams();
  const { user: currentUser } = useAuth();
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const [posts, setPosts] = useState([]);
  const [followers, setFollowers] = useState([]);
  const [following, setFollowing] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState("posts");
  const [showEditProfile, setShowEditProfile] = useState(false);
  const [selectedProfilePic, setSelectedProfilePic] = useState(null);
  const [profilePicPreview, setProfilePicPreview] = useState(null);
  const [bio, setBio] = useState("");
  const [uploading, setUploading] = useState(false);

  const isOwnProfile = !userId || (currentUser && userId === currentUser.id);

  const loadProfile = useCallback(async () => {
    try {
      const endpoint = userId ? `/profile/${userId}/` : "/profile/";
      const response = await axios.get(endpoint);
      setProfile(response.data);
      setBio(response.data.profile?.bio || "");
    } catch (error) {
      console.error("Error loading profile:", error);
    }
  }, [userId]);

  const loadPosts = useCallback(async () => {
    try {
      const endpoint = userId ? `/posts/user/${userId}/` : "/posts/my/";
      const response = await axios.get(endpoint);
      setPosts(response.data);
    } catch (error) {
      console.error("Error loading posts:", error);
    }
    setLoading(false);
  }, [userId]);

  useEffect(() => {
    loadProfile();
    loadPosts();
  }, [loadProfile, loadPosts]);

  const loadFollowers = async () => {
    try {
      const endpoint = userId ? `/followers/${userId}/` : "/followers/";
      const response = await axios.get(endpoint);
      setFollowers(response.data);
    } catch (error) {
      console.error("Error loading followers:", error);
    }
  };

  const loadFollowing = async () => {
    try {
      const endpoint = userId ? `/following/${userId}/` : "/following/";
      const response = await axios.get(endpoint);
      setFollowing(response.data);
    } catch (error) {
      console.error("Error loading following:", error);
    }
  };

  const handleFollow = async () => {
    if (!profile) return;

    try {
      if (profile.is_following) {
        await axios.delete(`/unfollow/${profile.id}/`);
      } else {
        await axios.post(`/follow/${profile.id}/`);
      }
      loadProfile();
    } catch (error) {
      console.error("Error toggling follow:", error);
    }
  };

  const handleProfilePicSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (!file.type.startsWith("image/")) {
        alert("Please select an image file");
        return;
      }

      if (file.size > 5 * 1024 * 1024) {
        alert("File size must be less than 5MB");
        return;
      }

      setSelectedProfilePic(file);

      const reader = new FileReader();
      reader.onload = (e) => {
        setProfilePicPreview(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleProfileUpdate = async (e) => {
    e.preventDefault();
    setUploading(true);

    try {
      const formData = new FormData();
      if (selectedProfilePic) {
        formData.append("profile_picture", selectedProfilePic);
      }
      formData.append("bio", bio);

      await axios.patch("/profile/picture/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setShowEditProfile(false);
      setSelectedProfilePic(null);
      setProfilePicPreview(null);
      loadProfile();
    } catch (error) {
      console.error("Error updating profile:", error);
      alert("Failed to update profile");
    }

    setUploading(false);
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
    if (tab === "followers" && followers.length === 0) {
      loadFollowers();
    } else if (tab === "following" && following.length === 0) {
      loadFollowing();
    }
  };

  const UserAvatar = ({ user, size = 40 }) => {
    return user.profile?.profile_picture_url ? (
      <img
        src={user.profile.profile_picture_url}
        alt="Profile"
        style={{
          width: `${size}px`,
          height: `${size}px`,
          borderRadius: "50%",
          objectFit: "cover",
          marginRight: "12px",
        }}
      />
    ) : (
      <div
        className="user-avatar"
        style={{
          width: `${size}px`,
          height: `${size}px`,
          fontSize: `${size / 2.5}px`,
          marginRight: "12px",
        }}
      >
        {user.username.charAt(0).toUpperCase()}
      </div>
    );
  };

  if (loading || !profile) {
    return (
      <div className="text-center p-3">
        <div className="loading-spinner"></div>
        <p>Loading profile...</p>
      </div>
    );
  }

  return (
    <div>
      <div className="card p-3 mb-3 text-center">
        <div
          style={{
            position: "relative",
            display: "inline-block",
            margin: "0 auto 16px",
          }}
        >
          {profile.profile?.profile_picture_url ? (
            <img
              src={profile.profile.profile_picture_url}
              alt="Profile"
              style={{
                width: "80px",
                height: "80px",
                borderRadius: "50%",
                objectFit: "cover",
                border: "2px solid var(--border-color)",
              }}
            />
          ) : (
            <div
              className="user-avatar"
              style={{
                width: "80px",
                height: "80px",
                fontSize: "32px",
              }}
            >
              {profile.username.charAt(0).toUpperCase()}
            </div>
          )}
          {isOwnProfile && (
            <button
              onClick={() => setShowEditProfile(true)}
              style={{
                position: "absolute",
                bottom: "0",
                right: "0",
                background: "var(--accent-color)",
                color: "white",
                border: "none",
                borderRadius: "50%",
                width: "24px",
                height: "24px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                cursor: "pointer",
              }}
            >
              <Camera size={12} />
            </button>
          )}
        </div>

        <h2 style={{ marginBottom: "8px" }}>{profile.username}</h2>

        {(profile.first_name || profile.last_name) && (
          <p className="text-secondary mb-2">
            {profile.first_name} {profile.last_name}
          </p>
        )}

        {profile.profile?.bio && (
          <p style={{ marginBottom: "16px", lineHeight: "1.4" }}>
            {profile.profile.bio}
          </p>
        )}

        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "40px",
            margin: "24px 0",
          }}
        >
          <div className="stat" onClick={() => handleTabChange("posts")}>
            <div className="stat-number">{profile.posts_count}</div>
            <div className="stat-label">posts</div>
          </div>
          <div className="stat" onClick={() => handleTabChange("followers")}>
            <div className="stat-number">{profile.followers_count}</div>
            <div className="stat-label">followers</div>
          </div>
          <div className="stat" onClick={() => handleTabChange("following")}>
            <div className="stat-number">{profile.following_count}</div>
            <div className="stat-label">following</div>
          </div>
        </div>

        {!isOwnProfile && (
          <button
            className={`btn ${
              profile.is_following ? "btn-secondary" : "btn-primary"
            }`}
            onClick={handleFollow}
            style={{
              display: "flex",
              alignItems: "center",
              gap: "8px",
              margin: "0 auto",
            }}
          >
            <UserPlus size={18} />
            {profile.is_following ? "Following" : "Follow"}
          </button>
        )}
      </div>

      {showEditProfile && (
        <div className="card p-3 mb-3">
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "16px",
            }}
          >
            <h3>Edit Profile</h3>
            <button
              onClick={() => setShowEditProfile(false)}
              style={{
                background: "none",
                border: "none",
                cursor: "pointer",
              }}
            >
              ✕
            </button>
          </div>

          <form onSubmit={handleProfileUpdate}>
            <div className="form-group">
              <label
                style={{
                  display: "block",
                  marginBottom: "8px",
                  fontWeight: "500",
                }}
              >
                Profile Picture
              </label>

              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: "16px",
                }}
              >
                <div style={{ position: "relative" }}>
                  {profilePicPreview ? (
                    <img
                      src={profilePicPreview}
                      alt="Preview"
                      style={{
                        width: "60px",
                        height: "60px",
                        borderRadius: "50%",
                        objectFit: "cover",
                        border: "2px solid var(--border-color)",
                      }}
                    />
                  ) : profile.profile?.profile_picture_url ? (
                    <img
                      src={profile.profile.profile_picture_url}
                      alt="Current"
                      style={{
                        width: "60px",
                        height: "60px",
                        borderRadius: "50%",
                        objectFit: "cover",
                        border: "2px solid var(--border-color)",
                      }}
                    />
                  ) : (
                    <div
                      className="user-avatar"
                      style={{
                        width: "60px",
                        height: "60px",
                        fontSize: "24px",
                      }}
                    >
                      {profile.username.charAt(0).toUpperCase()}
                    </div>
                  )}
                </div>

                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() =>
                    document.getElementById("profile-pic-input").click()
                  }
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "8px",
                  }}
                >
                  <Camera size={16} />
                  Change Photo
                </button>
              </div>

              <input
                id="profile-pic-input"
                type="file"
                accept="image/*"
                onChange={handleProfilePicSelect}
                style={{ display: "none" }}
              />
            </div>

            <div className="form-group">
              <label
                style={{
                  display: "block",
                  marginBottom: "8px",
                  fontWeight: "500",
                }}
              >
                Bio
              </label>
              <textarea
                value={bio}
                onChange={(e) => setBio(e.target.value)}
                className="form-input"
                placeholder="Tell people about yourself..."
                rows="3"
                maxLength="500"
              />
              <small className="text-secondary">
                {bio.length}/500 characters
              </small>
            </div>

            <div style={{ display: "flex", gap: "8px" }}>
              <button
                type="submit"
                className="btn btn-primary"
                disabled={uploading}
                style={{ flex: 1 }}
              >
                {uploading ? "Saving..." : "Save Changes"}
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => setShowEditProfile(false)}
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="card">
        <div
          style={{
            display: "flex",
            borderBottom: "1px solid var(--border-light)",
          }}
        >
          <button
            className={`feed-tab ${activeTab === "posts" ? "active" : ""}`}
            onClick={() => handleTabChange("posts")}
            style={{ flex: 1, borderRadius: 0 }}
          >
            <Grid size={18} style={{ marginRight: "8px" }} />
            Posts
          </button>
          <button
            className={`feed-tab ${activeTab === "followers" ? "active" : ""}`}
            onClick={() => handleTabChange("followers")}
            style={{ flex: 1, borderRadius: 0 }}
          >
            <Users size={18} style={{ marginRight: "8px" }} />
            Followers
          </button>
          <button
            className={`feed-tab ${activeTab === "following" ? "active" : ""}`}
            onClick={() => handleTabChange("following")}
            style={{ flex: 1, borderRadius: 0 }}
          >
            <Users size={18} style={{ marginRight: "8px" }} />
            Following
          </button>
        </div>

        <div className="p-3">
          {activeTab === "posts" && (
            <div>
              {posts.length === 0 ? (
                <div className="text-center p-3">
                  <Grid
                    size={48}
                    style={{
                      color: "var(--text-secondary)",
                      marginBottom: "16px",
                    }}
                  />
                  <h3 style={{ marginBottom: "8px" }}>No posts yet</h3>
                  <p className="text-secondary">
                    {isOwnProfile
                      ? "Share your first photo!"
                      : "No posts to show"}
                  </p>
                  {isOwnProfile && (
                    <button
                      className="btn btn-primary mt-2"
                      onClick={() => navigate("/create")}
                    >
                      Create Post
                    </button>
                  )}
                </div>
              ) : (
                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns:
                      "repeat(auto-fill, minmax(150px, 1fr))",
                    gap: "12px",
                  }}
                >
                  {posts.map((post) => (
                    <div
                      key={post.id}
                      style={{
                        aspectRatio: "1",
                        backgroundImage: `url(${
                          post.image_display_url || post.image_url
                        })`,
                        backgroundSize: "cover",
                        backgroundPosition: "center",
                        borderRadius: "8px",
                        cursor: "pointer",
                        border: "1px solid var(--border-color)",
                        transition: "transform 0.2s ease",
                      }}
                      onClick={() => navigate("/")}
                      onMouseEnter={(e) =>
                        (e.target.style.transform = "scale(1.02)")
                      }
                      onMouseLeave={(e) =>
                        (e.target.style.transform = "scale(1)")
                      }
                    />
                  ))}
                </div>
              )}
            </div>
          )}

          {activeTab === "followers" && (
            <div>
              {followers.length === 0 ? (
                <div className="text-center p-3">
                  <Users
                    size={48}
                    style={{
                      color: "var(--text-secondary)",
                      marginBottom: "16px",
                    }}
                  />
                  <h3 style={{ marginBottom: "8px" }}>No followers yet</h3>
                  <p className="text-secondary">
                    {isOwnProfile
                      ? "People who follow you will appear here"
                      : "No followers to show"}
                  </p>
                </div>
              ) : (
                <div>
                  {followers.map((user) => (
                    <div
                      key={user.id}
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center",
                        padding: "12px 0",
                        borderBottom: "1px solid var(--border-light)",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          alignItems: "center",
                          cursor: "pointer",
                          flex: 1,
                        }}
                        onClick={() => navigate(`/profile/${user.id}`)}
                      >
                        <UserAvatar user={user} />
                        <div>
                          <h4
                            style={{
                              margin: 0,
                              fontSize: "15px",
                              fontWeight: "600",
                            }}
                          >
                            {user.username}
                          </h4>
                          <p
                            style={{
                              margin: 0,
                              color: "var(--text-secondary)",
                              fontSize: "13px",
                            }}
                          >
                            {user.first_name} {user.last_name}
                          </p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {activeTab === "following" && (
            <div>
              {following.length === 0 ? (
                <div className="text-center p-3">
                  <Users
                    size={48}
                    style={{
                      color: "var(--text-secondary)",
                      marginBottom: "16px",
                    }}
                  />
                  <h3 style={{ marginBottom: "8px" }}>
                    Not following anyone yet
                  </h3>
                  <p className="text-secondary">
                    {isOwnProfile
                      ? "People you follow will appear here"
                      : "No following to show"}
                  </p>
                </div>
              ) : (
                <div>
                  {following.map((user) => (
                    <div
                      key={user.id}
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center",
                        padding: "12px 0",
                        borderBottom: "1px solid var(--border-light)",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          alignItems: "center",
                          cursor: "pointer",
                          flex: 1,
                        }}
                        onClick={() => navigate(`/profile/${user.id}`)}
                      >
                        <UserAvatar user={user} />
                        <div>
                          <h4
                            style={{
                              margin: 0,
                              fontSize: "15px",
                              fontWeight: "600",
                            }}
                          >
                            {user.username}
                          </h4>
                          <p
                            style={{
                              margin: 0,
                              color: "var(--text-secondary)",
                              fontSize: "13px",
                            }}
                          >
                            {user.first_name} {user.last_name}
                          </p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Profile;
