# Post Craft

[![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

**Post Craft** is a modern, responsive, and dark-themed blogging platform engineered with Django 6.0.3 and styled with Bootstrap 5.3.3. It is designed to offer an immersive, user-friendly reading and writing environment.

---

## Key Features

- **Premium Dark-Theme Interface**: A carefully designed dark layout with beautiful typography, clean card structures, and a polished Hero Banner for featured articles.
- **User Authentication & Profiles**: Secure user registration, login, and logout capabilities using customized forms and views.
- **Dynamic Categories Navigation**: Seamless category filtration supported by a custom context processor, making categories available globally in all views.
- **Global Full-Text Search**: Instantly find articles using the search view matching keywords in the title, description, or content.
- **Time-Ago Filter**: Custom template filters (e.g., `exact_naturaltime`) designed to simplify timestamps into highly readable formats (e.g., `"2 days ago"` instead of `"2 days, 2 hours ago"`).
- **SEO-friendly Slugs**: Clean, readable URLs using unique slugs for blog posts.

---

## Technology Stack

- **Backend Framework**: Django 6.0.3 (Python)
- **Frontend Framework**: Bootstrap 5.3.3 (CSS & JS)
- **Database**: SQLite (Local file-based system)
- **Static & Media Asset Handling**: Integrated Django static files & media uploads path

---

## File Structure

```text
Post Craft/
│
├── blog_main/                 # Global Settings & Configuration
│   ├── static/                # Static assets (custom css & assets)
│   ├── settings.py            # Global Django settings configuration
│   ├── urls.py                # Core URL dispatch router
│   ├── views.py               # Root view handlers (home page, user registration)
│   └── wsgi.py / asgi.py      # Entrypoints for production servers
│
├── blogs/                     # Primary Blogging Application
│   ├── templatetags/          # Custom Django filters & tags
│   │   └── custom_filters.py  # Cleans timestamps to standard natural time
│   ├── admin.py               # Customizations for Django Admin Panel
│   ├── context_processors.py  # Injects categories into all pages globally
│   ├── models.py              # Models for Categories and Blogs
│   ├── urls.py                # Feature routing for category filtering
│   └── views.py               # Feature view controllers (posts, categories, search)
│
├── templates/                 # Global HTML templates
│   ├── base.html              # Core parent template with navbar & footer
│   ├── home.html              # Homepage with Hero banner & article grids
│   ├── post.html              # Immersive individual article layout page
│   ├── posts_by_category.html # Filtered category listing page
│   ├── search.html            # Search results layout
│   └── login.html / register.html # Auth pages
│
├── db.sqlite3                 # Local database storage
├── manage.py                  # Django administrative command-line utility
└── README.md                  # Project documentation (this file)
```

---

## Installation & Setup

Follow these steps to run Post Craft locally:

### Prerequisites
- Python 3.10 or higher installed on your machine.
- Git (optional, for cloning the repository).

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Post-Craft.git
cd Post-Craft
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Django and Dependencies
```bash
pip install django pillow
```
*(Note: `pillow` is required for handling image uploads inside the database model).*

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to view the application, or access the admin panel at `http://127.0.0.1:8000/admin/` to add posts and categories.

---

## 🗺️ Roadmap & Future Features

We are actively developing Post Craft to evolve into a full-fledged content management platform. The following features are planned for future releases:

### 1. ✍️ In-App Interactive Blog Editor (CRUD)
- **Interactive WYSIWYG Editor**: Integrate rich text editors such as **TinyMCE** or **CKEditor** so authors can draft, style, add headers, format code blocks, and write content directly on the website.
- **Author Workspace Dashboard**: A dedicated dashboard for registered authors to view, edit, draft, and delete their own blog posts.
- **Live Preview Mode**: A side-by-side or modal preview window showing exactly how the blog post will appear when published.
- **Save as Draft / Schedule Publish**: Allow authors to write posts and save them as drafts or schedule them to be published automatically at a future date.

### 2. Media & Asset Library
- **Drag & Drop Upload**: A streamlined UI element inside the blog editor allowing quick photo and media uploads.
- **Image Cropper & Compression**: Automatic optimization and cropping tools for blog headers and inline images to ensure fast page loads.

### 3.Reader Engagement & Comments
- **Discussions System**: Threaded comments under blog posts for user interaction.


