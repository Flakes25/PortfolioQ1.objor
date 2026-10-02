# Wizard Portfolio

A modern, magical fantasy-themed portfolio website built with **Django**, featuring a cinematic landing page, animated stars, glowing cursor effects, a dark-themed user interface, and a secure admin-only dashboard.

---

## Features

- **Cinematic Landing Page & UI**: Dark-themed wizard aesthetic with smooth scrolling, glowing accents, and custom typography (`Cinzel` and `Cormorant Garamond`).
- **Dynamic Projects & Tech Stacks**: Projects linked via a Many-to-Many relationship with reusable tech stacks without data duplication.
- **Secure Admin Dashboard**: Protected by `@user_passes_test` and custom superuser authentication to manage projects and tech stacks.
- **Interactive Forms & Views**: Custom creation forms, public contact forms, and secure authentication and logout flows.

---

## Setup & Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Flakes25/PortfolioQ1.objor.git
cd PortfolioQ1.objor
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
1. Duplicate the provided `.env.example` file and rename the copy to `.env`:
   ```bash
   cp .env.example .env
   ```
   *(Note: Ensure your actual `.env`, `.venv/`, and `db.sqlite3` files remain untracked and excluded via `.gitignore`).*
2. Update your `.env` file with your local or production settings (e.g., `DEBUG=False`, unique `SECRET_KEY`).

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
*(You will use this superuser account to log into the custom `/login/` and access the `/dashboard/`).*

### 7. Run the Development Server
```bash
python manage.py runserver
```
Open your browser and visit:
- **Public Site:** `http://127.0.0.1:8000/`
- **Admin Dashboard & Login:** `http://127.0.0.1:8000/dashboard/`

---

## Project Structure

```
PortfolioWebsite/
│
├── portfolio/             # Django project settings & URL configuration
│
├── website/               # Main portfolio app
│   ├── templates/         # HTML templates (base, dashboard, core login, etc.)
│   ├── static/            # CSS stylesheets, images, and static assets
│   ├── views.py           # Public and protected admin dashboard views
│   ├── forms.py           # Django model forms for projects and tech stacks
│   ├── models.py          # Project and TechStack models (ManyToManyField)
│   └── urls.py            # App-level URL routing
│
├── manage.py
├── .env.example           # Environment variables template
├── .gitignore             # Excluded sensitive files (db.sqlite3, .env, venv)
└── README.md
```

---

## Git Workflow

This project follows a professional branch-based Git workflow:
- `main` — Production-ready release branch
- `feature/*` — Dedicated feature branches for ongoing development (e.g., admin dashboard and views)

Changes are thoroughly tested, committed with descriptive messages, and merged via Pull Requests.

---

## Author

**Mavei**  
GitHub: [https://github.com/Flakes25](https://github.com/Flakes25)