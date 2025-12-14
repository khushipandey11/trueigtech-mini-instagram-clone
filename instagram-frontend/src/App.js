import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import "./App.css";

import Header from "./components/Header";
import Login from "./components/Login";
import Feed from "./components/Feed";
import Profile from "./components/Profile";
import Search from "./components/Search";
import Notifications from "./components/Notifications";
import CreatePost from "./components/CreatePost";
import Stories from "./components/Stories";
import { AuthProvider, useAuth } from "./contexts/AuthContext";
import { ThemeProvider } from "./contexts/ThemeContext";

function AppContent() {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="App">
      <Router>
        {user && <Header />}
        <main className={user ? "main-content" : "auth-content"}>
          <Routes>
            <Route
              path="/login"
              element={!user ? <Login /> : <Navigate to="/" />}
            />
            <Route
              path="/"
              element={user ? <Feed /> : <Navigate to="/login" />}
            />
            <Route
              path="/search"
              element={user ? <Search /> : <Navigate to="/login" />}
            />
            <Route
              path="/notifications"
              element={user ? <Notifications /> : <Navigate to="/login" />}
            />
            <Route
              path="/profile/:userId?"
              element={user ? <Profile /> : <Navigate to="/login" />}
            />
            <Route
              path="/create"
              element={user ? <CreatePost /> : <Navigate to="/login" />}
            />
            <Route
              path="/stories"
              element={user ? <Stories /> : <Navigate to="/login" />}
            />
          </Routes>
        </main>
      </Router>
    </div>
  );
}

function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
