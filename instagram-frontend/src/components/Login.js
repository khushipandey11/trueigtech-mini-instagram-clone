import React, { useState } from "react";
import { Sun, Moon } from "lucide-react";
import { useAuth } from "../contexts/AuthContext";
import { useTheme } from "../contexts/ThemeContext";

const Login = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    email: "",
    first_name: "",
    last_name: "",
    password_confirm: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const { login, register } = useAuth();
  const { theme, toggleTheme } = useTheme();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      let result;
      if (isLogin) {
        result = await login({
          username: formData.username,
          password: formData.password,
        });
      } else {
        if (formData.password !== formData.password_confirm) {
          setError("Passwords don't match");
          setLoading(false);
          return;
        }
        result = await register(formData);
      }

      if (!result.success) {
        setError(
          typeof result.error === "string"
            ? result.error
            : "Authentication failed"
        );
      }
    } catch (err) {
      setError("Network error occurred");
    }

    setLoading(false);
  };

  const toggleMode = () => {
    setIsLogin(!isLogin);
    setError("");
    setFormData({
      username: "",
      password: "",
      email: "",
      first_name: "",
      last_name: "",
      password_confirm: "",
    });
  };

  return (
    <div className="auth-content">
      <div
        className="card"
        style={{ width: "100%", maxWidth: "400px", padding: "40px" }}
      >
        <div style={{ position: "absolute", top: "20px", right: "20px" }}>
          <button
            className="theme-toggle"
            onClick={toggleTheme}
            title={`Switch to ${theme === "dark" ? "light" : "dark"} mode`}
          >
            {theme === "dark" ? <Sun size={20} /> : <Moon size={20} />}
          </button>
        </div>

        <div className="text-center mb-3">
          <h1
            className="logo"
            style={{ fontSize: "32px", marginBottom: "8px" }}
          >
            📸 Instagram
          </h1>
          <h2 style={{ fontSize: "24px", marginBottom: "24px" }}>
            {isLogin ? "Welcome Back" : "Join Instagram"}
          </h2>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="text"
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              className="form-input"
              required
            />
          </div>

          <div className="form-group">
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              className="form-input"
              required
            />
          </div>

          {!isLogin && (
            <>
              <div className="form-group">
                <input
                  type="email"
                  name="email"
                  placeholder="Email"
                  value={formData.email}
                  onChange={handleChange}
                  className="form-input"
                  required
                />
              </div>

              <div className="form-group">
                <input
                  type="text"
                  name="first_name"
                  placeholder="First Name"
                  value={formData.first_name}
                  onChange={handleChange}
                  className="form-input"
                />
              </div>

              <div className="form-group">
                <input
                  type="text"
                  name="last_name"
                  placeholder="Last Name"
                  value={formData.last_name}
                  onChange={handleChange}
                  className="form-input"
                />
              </div>

              <div className="form-group">
                <input
                  type="password"
                  name="password_confirm"
                  placeholder="Confirm Password"
                  value={formData.password_confirm}
                  onChange={handleChange}
                  className="form-input"
                  required
                />
              </div>
            </>
          )}

          {error && <div className="error-message mb-2">{error}</div>}

          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={loading}
              style={{ width: "100%" }}
            >
              {loading ? "Please wait..." : isLogin ? "Log In" : "Sign Up"}
            </button>
          </div>
        </form>

        <div className="text-center mt-3">
          <p className="text-secondary">
            {isLogin ? "Don't have an account? " : "Already have an account? "}
            <button
              type="button"
              onClick={toggleMode}
              style={{
                background: "none",
                border: "none",
                color: "var(--accent-color)",
                cursor: "pointer",
                textDecoration: "underline",
              }}
            >
              {isLogin ? "Sign up" : "Log in"}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
