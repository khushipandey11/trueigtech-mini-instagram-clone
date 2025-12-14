# Instagram Clone - Frontend

React application for the Instagram clone. Clean, modern interface with dark mode support.

## Features

- **Authentication** - Login and signup with persistent sessions
- **Photo Sharing** - Upload files or use image URLs
- **Stories** - Create and view 24-hour temporary posts
- **Social Feed** - Following and explore feeds
- **User Profiles** - Custom profile pictures and bios
- **Search** - Find and follow other users
- **Notifications** - Real-time interaction alerts
- **Dark Mode** - Toggle between light and dark themes
- **Responsive** - Works great on mobile and desktop

## Quick Start

1. **Install packages**

   ```bash
   npm install
   ```

2. **Start the app**

   ```bash
   npm start
   ```

3. **Open your browser**
   Go to `http://localhost:3000`

## Project Structure

```
src/
├── components/          # React components
│   ├── Header.js       # Navigation bar
│   ├── Login.js        # Authentication
│   ├── Feed.js         # Main post feed
│   ├── Post.js         # Individual post
│   ├── Stories.js      # Stories view
│   ├── Profile.js      # User profiles
│   ├── Search.js       # User search
│   ├── CreatePost.js   # Post creation
│   └── Notifications.js # Notifications
├── contexts/           # State management
│   ├── AuthContext.js  # User authentication
│   └── ThemeContext.js # Dark/light mode
├── App.js             # Main app
├── App.css            # Global styles
└── index.js           # Entry point
```

## Key Components

**Header** - Navigation with theme toggle and notification badge

**Feed** - Displays posts with like/comment functionality, switches between following and explore modes

**Stories** - Grid view of active stories with creation form

**Profile** - User info, posts grid, followers/following lists, profile picture upload

**Search** - Real-time user search with follow buttons

**CreatePost** - File upload or URL input with image preview

## Styling

- CSS variables for consistent theming
- Dark and light mode support
- Responsive design for all screen sizes
- Smooth animations and transitions
- Clean, Instagram-inspired interface

## State Management

- **AuthContext** - Handles user login, logout, and authentication state
- **ThemeContext** - Manages dark/light mode preference
- **Component State** - Local state for forms and UI interactions

## API Integration

All API calls use Axios with automatic JWT token handling. The app communicates with the Django backend for all data operations.

## Development

**Adding New Features**

- Create new components in `src/components/`
- Add routes in `App.js`
- Update navigation in `Header.js`

**Styling**

- Global styles in `App.css`
- Use CSS variables for consistent theming
- Follow existing component patterns

**State**

- Use React hooks for local state
- Add to contexts for global state
- Keep components focused and reusable

## Build for Production

```bash
npm run build
```

Creates optimized production build in `build/` folder.
