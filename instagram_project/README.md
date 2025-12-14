# Instagram Clone – Backend

This is a simple **Django REST API** for an Instagram-like application. I built this project as part of a coding round to demonstrate backend concepts like authentication, relationships, and API design.

The main focus of this project is **functionality and clarity**, not advanced features.

---

## What this project does

- Users can sign up and log in
- Users can follow and unfollow other users
- Logged-in users can create posts
- Posts contain an **image URL** and a caption
- Users can like and unlike posts
- Users can comment on posts
- Each user gets a feed showing posts from people they follow

---

## Tech Stack

- **Backend:** Django
- **API Framework:** Django REST Framework (DRF)
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite
- **API Testing:** Postman

I chose Django REST Framework because it allows fast and secure backend development.

---

## API Endpoints

### Authentication

- `POST /api/register/` – User signup
- `POST /api/login/` – User login (JWT token)

### Posts

- `POST /api/posts/` – Create a post
- `GET /api/feed/` – Feed (posts from followed users)
- `POST /api/posts/<id>/like/` – Like / unlike a post
- `POST /api/posts/<id>/comment/` – Add a comment

### Follow System

- `POST /api/follow/<id>/` – Follow a user
- `POST /api/unfollow/<id>/` – Unfollow a user

### Profile

- `GET /api/profile/<id>/` – View user profile

---

## Models Used

- **User** – Custom user model with followers and following
- **Post** – Stores image URL, caption, likes, and creator
- **Comment** – Stores comments on posts

Relationships are handled using Django ORM and foreign keys.

---

## How to Run the Project

1. Create and activate virtual environment

2. Install dependencies:

```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the server:

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## Notes

- Images are stored as **URLs**, not file uploads
- Frontend can be connected easily using Fetch or Axios
- Project focuses on backend logic and API correctness

---

## Why this approach

Given limited time, I focused on completing all core features correctly rather than adding complex or optional features. This project demonstrates my understanding of backend development, REST APIs, and database relationships.

---

Thank you for reviewing this project 🙂
