🧾 Expense Tracker API

A simple Expense Tracker API built with Django REST Framework and JWT Authentication (SimpleJWT).
Users can register, authenticate, and manage their categories & expenses securely with PostgreSQL as the database.

🚀 Features

✅ User registration & JWT authentication

✅ PostgreSQL database support

✅ Category & Expense management (user-specific)

✅ Monthly summary reports (grouped by category)

✅ Token-based permissions (users only access their own data)

🛠️ Tech Stack

Backend: Django, Django REST Framework

Auth: JWT via djangorestframework-simplejwt

Database: PostgreSQL

Language: Python 3.10+

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/expense-tracker-api.git
cd expense-tracker-api

2️⃣ Create & activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup PostgreSQL database

Create a PostgreSQL database and update your settings.py (or .env file):

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "expense_tracker",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

5️⃣ Apply migrations
python manage.py migrate

6️⃣ Run server
python manage.py runserver

🔑 Authentication

This project uses JWT Authentication (SimpleJWT).

Configure token expiry (in settings.py):
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

📡 API Endpoints
👤 User Registration & List

URL: http://127.0.0.1:8000/api/users/

Method: POST → Register new user

Method: GET → List all users (admin/superuser access recommended)

Payload (POST):

{
  "username": "test",
  "email": "test@example.com",
  "first_name": "test",
  "last_name": "1",
  "password": "examble123"
}

🔑 Login (JWT Token)

URL: http://127.0.0.1:8000/api/auth/login/

Method: POST → Obtain access & refresh token

Payload:

{
  "username": "test",
  "password": "examble123"
}

📂 Categories

URL: http://127.0.0.1:8000/api/categories/

Method: POST → Create category

Method: GET → List categories (only user’s own categories)

Payload (POST):

{
  "name": "Shopping"
}

💰 Expenses

URL: http://127.0.0.1:8000/api/expenses/

Method: POST → Create expense

Method: GET → List expenses (only user’s own expenses)

Payload (POST):

{
  "category": 1,
  "amount": "55.00",
  "date": "2025-01-26",
  "description": "Vegetables"
}

📌 Expense Detail (Retrieve, Update, Delete)

URL: http://127.0.0.1:8000/api/expenses/{id}/

Method: GET → Retrieve expense

Method: PATCH → Update expense

Method: DELETE → Delete expense

Payload (PATCH example):

{
  "category": 1,
  "amount": "75.00",
  "date": "2025-05-26",
  "description": "Vegetables",
  "created_at": "2025-09-26T10:58:58.975065Z"
}

📊 Monthly Reports

URL:

http://127.0.0.1:8000/api/reports/monthly-summary/?year=2025&month=05


Method: GET → Summary of expenses by category

✅ Permissions

🔒 Authentication is required for all endpoints (except user registration and categor create and list).
