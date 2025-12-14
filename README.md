# Instagram Clone

A full-featured social media app built with Django and React. Share photos, follow friends, post stories, and stay connected.

## What's Inside

This is a complete Instagram-style social platform with all the features you'd expect:

- **Photo Sharing** - Upload images or use URLs to share moments
- **Stories** - 24-hour temporary posts that disappear automatically
- **Social Features** - Follow users, like posts, leave comments
- **Real-time Notifications** - Get notified when someone interacts with your content
- **User Profiles** - Custom profile pictures and bios
- **Search & Discovery** - Find new people to follow
- **Dark Mode** - Easy on the eyes theme switching

## Quick Start

### What You Need

- Python 3.8 or newer
- Node.js 16 or newer
- Basic terminal knowledge

### Backend Setup

1. **Get the code**

   ```bash
   git clone <repository-url>
   cd instagram_project
   ```

2. **Install Python packages**

   ```bash
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers pillow
   ```

3. **Set up the database**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the server**
   ```bash
   python manage.py runserver
   ```

The backend will be running at `http://localhost:8000`

### Frontend Setup

1. **Open a new terminal and go to the frontend folder**

   ```bash
   cd instagram-frontend
   ```

2. **Install packages**

   ```bash
   npm install
   ```

3. **Start the app**
   ```bash
   npm start
   ```

The app will open at `http://localhost:3000`

## How to Use

### Getting Started

1. Open `http://localhost:3000` in your browser
2. Sign up for a new account or log in
3. Start sharing photos and following people

### Main Features

**Posting Photos**

- Click "Create" in the navigation
- Upload a file or paste an image URL
- Add a caption and share

**Stories**

- Click "Stories" to view or create stories
- Stories disappear after 24 hours automatically
- Add text overlays to your story images

**Profile Setup**

- Go to your profile page
- Click the camera icon on your profile picture to upload a new one
- Add a bio to tell people about yourself

**Social Interaction**

- Like posts by clicking the heart icon
- Leave comments on any post
- Follow users from search or their profiles
- Get notifications when people interact with your content

## Project Structure

```
instagram_project/          # Django backend
├── instagram_app/         # Main app with models and APIs
├── media/                 # Uploaded images storage
└── manage.py             # Django management

instagram-frontend/        # React frontend
├── src/
│   ├── components/       # UI components
│   ├── contexts/         # App state management
│   └── App.js           # Main app component
└── package.json         # Dependencies
```

## Tech Stack

**Backend**

- Django - Web framework
- Django REST Framework - API building
- JWT - User authentication
- SQLite - Database (easily changeable)
- Pillow - Image processing

**Frontend**

- React - User interface
- Axios - API requests
- React Router - Navigation
- Lucide React - Icons

## Development Tips

**Adding New Features**

- Backend changes go in `instagram_project/instagram_app/`
- Frontend components go in `instagram-frontend/src/components/`
- API endpoints are defined in `urls.py`

**File Uploads**

- Images are stored in `instagram_project/media/`
- Both file uploads and URLs are supported
- File size limit is 10MB for posts, 5MB for profile pictures

**Database Changes**

- After modifying models, run:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

## Troubleshooting

**Backend won't start**

- Make sure all Python packages are installed
- Check that port 8000 isn't already in use

**Frontend won't start**

- Run `npm install` to make sure all packages are installed
- Check that port 3000 isn't already in use

**Images not loading**

- Make sure the Django server is running
- Check that the `media` folder exists in the backend directory

**Can't upload files**

- Verify Pillow is installed: `pip install pillow`
- Check file size (must be under 10MB)
- Make sure the file is a valid image format

## Production Notes

This setup is perfect for development and learning. For production use, you'd want to:

- Use a proper database like PostgreSQL
- Set up proper file storage (AWS S3, etc.)
- Configure environment variables
- Set up proper security headers
- Use a production web server

## Contributing

Feel free to fork this project and make it your own. Some ideas for improvements:

- Video support for posts and stories
- Direct messaging between users
- Post sharing and reposting
- Advanced search and filtering
- Mobile app version

## License

This project is open source and available for learning and personal use.
