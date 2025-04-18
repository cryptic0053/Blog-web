# 📝 Blog Web – A Django Blogging Platform

> A modern and responsive blog web app built using Django and Bootstrap 4.  
> Users can register, log in, create blog posts, comment, like, and explore blogs via tags and categories.
> Check it out:https://blog-web-6.onrender.com/

---

## 🚀 Features

- 🔐 User registration & authentication (login/signup/logout)
- 📝 Create, update, and delete blog posts
- 💬 Comment system for posts
- 📊 Like button + view counter
- 🔎 Search blog posts by keyword
- 🔖 Filter posts by categories and tags
- 📱 Responsive layout using Bootstrap 4
- 📂 Clean code structure following Django best practices

---

## 🛠️ Tech Stack

| Layer         | Technology                  |
|---------------|------------------------------|
| 🧠 Backend     | Django 5.1                   |
| 🎨 Frontend    | HTML, CSS, Bootstrap 4       |
| 🗄️ Database    | SQLite (default) / PostgreSQL |
| ☁ Deployment  | [Render.com](https://render.com)  |

---

## 📦 Installation (Local)

```bash
# 1. Clone the repo
git clone https://github.com/cryptic0053/Blog-web.git
cd Blog-web

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
