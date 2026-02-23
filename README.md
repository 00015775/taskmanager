# TaskManager

A full-stack task management web application built with Django, containerized with Docker, and deployed with a complete CI/CD pipeline.

## Features

- User authentication (register, login, logout, profile)
- Create, read, update, and delete tasks
- Filter tasks by status, priority, and tag
- Tag management with custom colors
- Dashboard with task statistics
- Admin panel for data management
- PostgreSQL database with proper relationships
- Dockerized with Nginx + Gunicorn for production
- Automated CI/CD pipeline via GitHub Actions

## Technologies Used

- **Backend:** Django 4.2, Python 3.11, Gunicorn
- **Database:** PostgreSQL 15
- **Frontend:** Bootstrap 5, Font Awesome
- **Containerization:** Docker, Docker Compose
- **Web Server:** Nginx
- **CI/CD:** GitHub Actions
- **Cloud:** Eskiz Cloud Server
- **SSL:** Let's Encrypt (Certbot)

## Local Setup Instructions

### Prerequisites
- Python 3.11+
- Docker Desktop
- Git

### Option A — Run with Docker (recommended)

1. Clone the repository:
```bash
   git clone https://github.com/00015775/taskmanager.git
   cd taskmanager
```

2. Create your `.env` file from the example:
```bash
   cp .env.example .env
```

3. Edit `.env` with your values (see Environment Variables section below)

4. Build and start all containers:
```bash
   docker compose up --build
```

5. Visit `http://localhost` in your browser (Chromium-based)

6. Create a superuser for admin access:
```bash
   docker compose exec web python manage.py createsuperuser
```

### Option B — Run locally without Docker

1. Clone and enter the project:
```bash
   git clone https://github.com/00015775/taskmanager.git
   cd taskmanager
```

2. Create and activate virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run migrations:
```bash
   python manage.py migrate
```

5. Start the development server:
```bash
   python manage.py runserver
```

6. Visit `http://127.0.0.1:8000`

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key (keep this secret) | `django-insecure-...` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` |
| `POSTGRES_DB` | PostgreSQL database name | `taskmanager` |
| `POSTGRES_USER` | PostgreSQL username | `taskmanager_user` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `strongpassword` |
| `POSTGRES_HOST` | PostgreSQL host (use `db` inside Docker) | `db` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` |
| `SECURE_SSL_REDIRECT` | Enable HTTPS redirect (True in production) | `False` |

## Deployment Instructions

### Server Requirements
- Ubuntu 22.04
- Docker + Docker Compose installed
- Domain name pointed to server IP

### Steps

1. SSH into your server:
```bash
   ssh username@your-server-ip
```

2. Clone the repository:
```bash
   git clone https://github.com/00015775/taskmanager.git
   cd taskmanager
```

3. Create production `.env`:
```bash
   cp .env.example .env
   nano .env  # fill in production values
```

4. Start containers:
```bash
   docker compose up -d
```

5. Install SSL certificate:
```bash
   sudo apt install certbot
   sudo certbot --nginx -d yourdomain.uz
```

6. Set `SECURE_SSL_REDIRECT=True` in `.env` and restart:
```bash
   docker compose restart
```

## Project Structure
```
taskmanager/
├── accounts/          # Authentication app
├── tasks/             # Task management app
├── core/              # Dashboard and shared views
├── taskmanager/       # Django project settings
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
├── templates/         # HTML templates
├── static/            # CSS, JS assets
├── nginx/             # Nginx configuration
├── docker/            # Entrypoint script
├── .github/workflows/ # CI/CD pipeline
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Screenshots

<video src="screenshots/app.mp4" controls width="100%" height="auto">
  Your browser does not support the video tag.
</video>

<img src="screenshots/dashboard.png" width="200" alt="Dashboard" />
<img src="screenshots/login.png" width="200" alt="Login" />
<img src="screenshots/profile.png" width="200" alt="Profile" />
<img src="screenshots/taskedit.png" width="200" alt="Task details" />
<img src="screenshots/tasklist.png" width="200" alt="Task list" />


## Running Tests
```bash
# Without Docker
pytest

# With Docker
docker compose exec web pytest
```

## CI/CD Pipeline

Every push to `main` branch automatically:
1. Runs code quality checks (flake8)
2. Runs all tests (pytest)
3. Builds Docker image
4. Pushes image to Docker Hub
5. Deploys to production server via SSH
6. Runs migrations and restarts services


