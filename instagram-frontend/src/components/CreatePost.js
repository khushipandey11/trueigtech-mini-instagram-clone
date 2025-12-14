import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Image, Send, Upload, X } from "lucide-react";
import axios from "axios";

const CreatePost = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [caption, setCaption] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();

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
      setSuccess("");

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
    setSuccess("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedFile) {
      setError("Please select an image file");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("image", selectedFile);
      formData.append("caption", caption);

      await axios.post("/posts/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setSuccess("Post created successfully!");

      setSelectedFile(null);
      setImagePreview(null);
      setCaption("");

      setTimeout(() => {
        navigate("/");
      }, 1500);
    } catch (error) {
      setError(error.response?.data?.detail || "Failed to create post");
    }

    setLoading(false);
  };

  return (
    <div>
      <div className="card p-3">
        <div className="text-center mb-3">
          <Image
            size={48}
            style={{ color: "var(--accent-color)", marginBottom: "16px" }}
          />
          <h2 style={{ marginBottom: "8px" }}>Create New Post</h2>
          <p className="text-secondary">
            Upload an image and share with your followers
          </p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label
              style={{
                display: "block",
                marginBottom: "8px",
                fontWeight: "500",
                color: "var(--text-primary)",
              }}
            >
              Select Image *
            </label>

            {!selectedFile ? (
              <div
                style={{
                  border: "2px dashed var(--border-color)",
                  borderRadius: "8px",
                  padding: "40px",
                  textAlign: "center",
                  cursor: "pointer",
                  transition: "border-color 0.2s ease",
                  backgroundColor: "var(--bg-tertiary)",
                }}
                onClick={() => document.getElementById("file-input").click()}
                onDragOver={(e) => {
                  e.preventDefault();
                  e.currentTarget.style.borderColor = "var(--accent-color)";
                }}
                onDragLeave={(e) => {
                  e.currentTarget.style.borderColor = "var(--border-color)";
                }}
                onDrop={(e) => {
                  e.preventDefault();
                  e.currentTarget.style.borderColor = "var(--border-color)";
                  const files = e.dataTransfer.files;
                  if (files.length > 0) {
                    const event = { target: { files } };
                    handleFileSelect(event);
                  }
                }}
              >
                <Upload
                  size={48}
                  style={{
                    color: "var(--text-secondary)",
                    marginBottom: "16px",
                  }}
                />
                <p
                  style={{ marginBottom: "8px", color: "var(--text-primary)" }}
                >
                  Click to select or drag and drop an image
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
              id="file-input"
              type="file"
              accept="image/*"
              onChange={handleFileSelect}
              style={{ display: "none" }}
            />
          </div>

          <div className="form-group">
            <label
              style={{
                display: "block",
                marginBottom: "8px",
                fontWeight: "500",
                color: "var(--text-primary)",
              }}
            >
              Caption
            </label>
            <textarea
              placeholder="Write a caption..."
              value={caption}
              onChange={(e) => setCaption(e.target.value)}
              className="form-input"
              rows="3"
              maxLength="2000"
              style={{ resize: "vertical", minHeight: "80px" }}
            />
            <small className="text-secondary">
              {caption.length}/2000 characters
            </small>
          </div>

          {error && <div className="error-message mb-2">{error}</div>}

          {success && <div className="success-message mb-2">{success}</div>}

          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={loading || !selectedFile}
              style={{
                width: "100%",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: "8px",
              }}
            >
              <Send size={18} />
              {loading ? "Creating Post..." : "Share Post"}
            </button>
          </div>
        </form>

        <div className="text-center mt-3">
          <button
            className="btn btn-secondary"
            onClick={() => navigate("/")}
            style={{ textDecoration: "none" }}
          >
            Cancel
          </button>
        </div>
      </div>

      <div className="card p-3 mt-3">
        <h4 style={{ marginBottom: "12px" }}>💡 Tips for great posts:</h4>
        <ul style={{ paddingLeft: "20px", color: "var(--text-secondary)" }}>
          <li>Use high-quality images (JPG, PNG, GIF)</li>
          <li>Write engaging captions</li>
          <li>Keep file sizes under 10MB for faster uploads</li>
          <li>You can drag and drop files directly</li>
          <li>Square images work best for the feed</li>
        </ul>
      </div>
    </div>
  );
};

export default CreatePost;
