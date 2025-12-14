import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Search as SearchIcon } from "lucide-react";
import axios from "axios";

const Search = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const searchUsers = useCallback(async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        `/users/search/?q=${encodeURIComponent(query)}`
      );
      setResults(response.data);
    } catch (error) {
      console.error("Search error:", error);
    }
    setLoading(false);
  }, [query]);

  useEffect(() => {
    const searchTimeout = setTimeout(() => {
      if (query.length >= 2) {
        searchUsers();
      } else {
        setResults([]);
      }
    }, 300);

    return () => clearTimeout(searchTimeout);
  }, [query, searchUsers]);

  const handleFollow = async (userId, isFollowing) => {
    try {
      if (isFollowing) {
        await axios.delete(`/unfollow/${userId}/`);
      } else {
        await axios.post(`/follow/${userId}/`);
      }
      setResults(
        results.map((user) =>
          user.id === userId ? { ...user, is_following: !isFollowing } : user
        )
      );
    } catch (error) {
      console.error("Error toggling follow:", error);
    }
  };

  return (
    <div>
      <div className="card p-3 mb-3">
        <div style={{ position: "relative" }}>
          <SearchIcon
            size={20}
            style={{
              position: "absolute",
              left: "12px",
              top: "50%",
              transform: "translateY(-50%)",
              color: "var(--text-secondary)",
            }}
          />
          <input
            type="text"
            placeholder="Search users..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="form-input"
            style={{ paddingLeft: "44px" }}
            autoFocus
          />
        </div>

        {loading && (
          <div className="text-center mt-2">
            <div
              className="loading-spinner"
              style={{ width: "20px", height: "20px" }}
            ></div>
          </div>
        )}

        {results.length === 0 && query.length >= 2 && !loading && (
          <p className="text-center text-secondary mt-2">No users found</p>
        )}

        {results.length > 0 && (
          <div style={{ marginTop: "16px" }}>
            {results.map((user) => (
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
                  {user.profile?.profile_picture_url ? (
                    <img
                      src={user.profile.profile_picture_url}
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
                    <div
                      className="user-avatar"
                      style={{ marginRight: "12px" }}
                    >
                      {user.username.charAt(0).toUpperCase()}
                    </div>
                  )}
                  <div>
                    <h4
                      style={{ margin: 0, fontSize: "15px", fontWeight: "600" }}
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

                <button
                  className={`btn ${
                    user.is_following ? "btn-secondary" : "btn-primary"
                  }`}
                  onClick={() => handleFollow(user.id, user.is_following)}
                  style={{ padding: "6px 16px", fontSize: "12px" }}
                >
                  {user.is_following ? "Following" : "Follow"}
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      {query.length < 2 && (
        <div className="card p-3 text-center">
          <SearchIcon
            size={48}
            style={{ color: "var(--text-secondary)", marginBottom: "16px" }}
          />
          <h3 style={{ marginBottom: "8px" }}>Search for users</h3>
          <p className="text-secondary">
            Type at least 2 characters to start searching for users to follow
          </p>
        </div>
      )}
    </div>
  );
};

export default Search;
