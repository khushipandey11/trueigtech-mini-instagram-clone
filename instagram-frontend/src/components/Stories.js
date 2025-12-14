import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Camera, Upload, X, Send } from "lucide-react";
import axios from "axios";

const Stories = () => {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [text, setText] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const loadStories = useCallback(async () => {
    setLoading(true);
    try {
      const response = await axios.get("/stories/");
      setStories(response.data);
    } catch (error) {
      console.error("Error loading stories:", error);
    }
    setLoading(false);
  }, []);

  useEffect(() => {
    loadStories();
  }, [loadStories]);

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (!file.type.startsWith("image/")) {
        setError("Please select an image file");
        return;
      }

      if (file.size > 10 * 1024 * 1024) {
        setError("File size must be less than 10MB");
        return;
      }

      setSelectedFile(file);
      setError("");

      const reader = new FileReader();
      reader.onload = (e) => {
        setImagePreview(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const clearImage = () => {
    setSelectedFile(null);
    setImagePreview(null);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedFile) {
      setError("Please select an image file");
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("image", selectedFile);
      formData.append("text", text);

      await axios.post("/stories/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setSelectedFile(null);
      setImagePreview(null);
      setText("");
      setShowCreateForm(false);
      loadStories();
    } catch (error) {
      setError(error.response?.data?.detail || "Failed to create story");
    }

    setSubmitting(false);
  };

  const formatTime = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffInHours = Math.floor((now - date) / (1000 * 60 * 60));

    if (diffInHours < 1) return "Just now";
    if (diffInHours < 24) return `${diffInHours}h ago`;
    return "Expired";
  };

  if (loading) {
    return (
      <div className="text-center p-3">
        <div className="loading-spinner"></div>
        <p>Loading stories...</p>
      </div>
    );
  }

  return (
    <div>
      <div className="card p-3 mb-3">
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <h2>Stories</h2>
          <button
            className="btn btn-primary"
            onClick={() => setShowCreateForm(!showCreateForm)}
            style={{ display: "flex", alignItems: "center", gap: "8px" }}
          >
            <Camera size={18} />
            Add Story
          </button>
        </div>
      </div>

      {showCreateForm && (
        <div className="card p-3 mb-3">
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "16px",
            }}
          >
            <h3>Create Story</h3>
            <button
              onClick={() => setShowCreateForm(false)}
              style={{ background: "none", border: "none", cursor: "pointer" }}
            >
              <X size={20} />
            </button>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="form-group">
              {!selectedFile ? (
                <div
                  style={{
                    border: "2px dashed var(--border-color)",
                    borderRadius: "8px",
                    padding: "40px",
                    textAlign: "center",
                    cursor: "pointer",
                    backgroundColor: "var(--bg-tertiary)",
                  }}
                  onClick={() =>
                    document.getElementById("story-file-input").click()
                  }
                >
                  <Upload
                    size={48}
                    style={{
                      color: "var(--text-secondary)",
                      marginBottom: "16px",
                    }}
                  />
                  <p
                    style={{
                      marginBottom: "8px",
                      color: "var(--text-primary)",
                    }}
                  >
                    Click to select an image
                  </p>
                  <p className="text-secondary" style={{ fontSize: "14px" }}>
                    Supports: JPG, PNG, GIF (Max 10MB)
                  </p>
                </div>
              ) : (
                <div style={{ position: "relative" }}>
                  <img
                    src={imagePreview}
                    alt="Preview"
                    style={{
                      width: "100%",
                      maxHeight: "400px",
                      objectFit: "cover",
                      borderRadius: "8px",
                      border: "1px solid var(--border-color)",
                    }}
                  />
                  <button
                    type="button"
                    onClick={clearImage}
                    style={{
                      position: "absolute",
                      top: "8px",
                      right: "8px",
                      background: "rgba(0, 0, 0, 0.7)",
                      color: "white",
                      border: "none",
                      borderRadius: "50%",
                      width: "32px",
                      height: "32px",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      cursor: "pointer",
                    }}
                  >
                    <X size={16} />
                  </button>
                </div>
              )}

              <input
                id="story-file-input"
                type="file"
                accept="image/*"
                onChange={handleFileSelect}
                style={{ display: "none" }}
              />
            </div>

            <div className="form-group">
              <input
                type="text"
                placeholder="Add text to your story..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                className="form-input"
                maxLength="200"
              />
              <small className="text-secondary">
                {text.length}/200 characters
              </small>
            </div>

            {error && <div className="error-message mb-2">{error}</div>}

            <button
              type="submit"
              className="btn btn-primary"
              disabled={submitting || !selectedFile}
              style={{
                width: "100%",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: "8px",
              }}
            >
              <Send size={18} />
              {submitting ? "Sharing..." : "Share Story"}
            </button>
          </form>
        </div>
      )}

      {stories.length === 0 ? (
        <div className="card p-3 text-center">
          <Camera
            size={48}
            style={{ color: "var(--text-secondary)", marginBottom: "16px" }}
          />
          <h3 style={{ marginBottom: "8px" }}>No stories yet</h3>
          <p className="text-secondary">
            Stories from people you follow will appear here
          </p>
        </div>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))",
            gap: "16px",
          }}
        >
          {stories.map((story) => (
            <div key={story.id} className="card" style={{ overflow: "hidden" }}>
              <div style={{ position: "relative" }}>
                <img
                  src={story.image_display_url || story.image_url}
                  alt="Story"
                  style={{
                    width: "100%",
                    height: "250px",
                    objectFit: "cover",
                  }}
                  onError={(e) => {
                    e.target.src =
                      "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjI1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkltYWdlIG5vdCBmb3VuZDwvdGV4dD48L3N2Zz4=";
                  }}
                />
                {story.text && (
                  <div
                    style={{
                      position: "absolute",
                      bottom: "0",
                      left: "0",
                      right: "0",
                      background:
                        "linear-gradient(transparent, rgba(0,0,0,0.7))",
                      color: "white",
                      padding: "16px",
                      fontSize: "14px",
                    }}
                  >
                    {story.text}
                  </div>
                )}
              </div>
              <div className="p-2">
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      cursor: "pointer",
                    }}
                    onClick={() => navigate(`/profile/${story.user.id}`)}
                  >
                    {story.user.profile?.profile_picture_url ? (
                      <img
                        src={story.user.profile.profile_picture_url}
                        alt="Profile"
                        style={{
                          width: "24px",
                          height: "24px",
                          borderRadius: "50%",
                          objectFit: "cover",
                          marginRight: "8px",
                        }}
                      />
                    ) : (
                      <div
                        className="user-avatar"
                        style={{
                          width: "24px",
                          height: "24px",
                          fontSize: "12px",
                          marginRight: "8px",
                        }}
                      >
                        {story.user.username.charAt(0).toUpperCase()}
                      </div>
                    )}
                    <span style={{ fontSize: "14px", fontWeight: "600" }}>
                      {story.user.username}
                    </span>
                  </div>
                  <span className="text-secondary" style={{ fontSize: "12px" }}>
                    {formatTime(story.created_at)}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Stories;
