import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import {
  Home,
  Search,
  Bell,
  User,
  Plus,
  LogOut,
  Sun,
  Moon,
  Camera,
} from "lucide-react";
import { useAuth } from "../contexts/AuthContext";
import { useTheme } from "../contexts/ThemeContext";
import axios from "axios";

const Header = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const [notificationCount, setNotificationCount] = useState(0);

  useEffect(() => {
    loadNotificationCount();
    const interval = setInterval(loadNotificationCount, 30000);
    return () => clearInterval(interval);
  }, []);

  const loadNotificationCount = async () => {
    try {
      const response = await axios.get("/notifications/");
      const unreadCount = response.data.filter((n) => !n.is_read).length;
      setNotificationCount(unreadCount);
    } catch (error) {
      console.error("Error loading notification count:", error);
    }
  };

  const isActive = (path) => location.pathname === path;

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="logo" onClick={() => navigate("/")}>
          📸 Instagram
        </div>

        <nav className="nav-buttons">
          <button
            className="theme-toggle"
            onClick={toggleTheme}
            title={`Switch to ${theme === "dark" ? "light" : "dark"} mode`}
          >
            {theme === "dark" ? <Sun size={20} /> : <Moon size={20} />}
          </button>

          <button
            className={`nav-btn ${isActive("/") ? "active" : ""}`}
            onClick={() => navigate("/")}
          >
            <Home size={18} />
            <span>Home</span>
          </button>

          <button
            className={`nav-btn ${isActive("/search") ? "active" : ""}`}
            onClick={() => navigate("/search")}
          >
            <Search size={18} />
            <span>Search</span>
          </button>

          <button
            className={`nav-btn ${isActive("/stories") ? "active" : ""}`}
            onClick={() => navigate("/stories")}
          >
            <Camera size={18} />
            <span>Stories</span>
          </button>

          <button
            className={`nav-btn ${isActive("/notifications") ? "active" : ""}`}
            onClick={() => navigate("/notifications")}
            style={{ position: "relative" }}
          >
            <Bell size={18} />
            <span>Notifications</span>
            {notificationCount > 0 && (
              <span className="notification-badge">
                {notificationCount > 99 ? "99+" : notificationCount}
              </span>
            )}
          </button>

          <button
            className={`nav-btn ${isActive("/create") ? "active" : ""}`}
            onClick={() => navigate("/create")}
          >
            <Plus size={18} />
            <span>Create</span>
          </button>

          <button
            className={`nav-btn ${isActive("/profile") ? "active" : ""}`}
            onClick={() => navigate("/profile")}
          >
            <User size={18} />
            <span>Profile</span>
          </button>

          <button className="nav-btn" onClick={handleLogout}>
            <LogOut size={18} />
            <span>Logout</span>
          </button>
        </nav>
      </div>
    </header>
  );
};

export default Header;
