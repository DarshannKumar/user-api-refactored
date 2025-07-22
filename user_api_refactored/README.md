# 🧑‍💻 User Management API (Refactored Flask Project)

A clean, modular Flask-based User Management System supporting basic CRUD operations, search, and login functionality. Fully secured and production-ready with SQLite integration.

---

## 🚀 Getting Started

### ✅ 1. Clone the Project

```bash
git clone https://github.com/DarshannKumar/user-api-refactored.git
cd user-api-refactored

on windows:
python -m venv venv
.\venv\Scripts\activate


on macos:
python3 -m venv venv
source venv/bin/activate


pip install Flask==2.3.2 Werkzeug==2.3.6

pip install -r requirements.txt

This creates a users.db SQLite database with a users table and 3 sample users.

cd user_api_refactored
python init_db.py
cd ..

You will see:
(venv) python -m user_api_refactored.app

server will start in:
http://localhost:5009/

🧪 Testing the API
You can test this API using:

✅ Postman

✅ REST Client VS Code Extension (.http file)

Example POST request for creating a user:

bash
Copy
Edit
POST http://localhost:5009/users
Content-Type: application/json

{
  "name": "Test User",
  "email": "test@example.com",
  "password": "123456"
}
✅ Project Structure
markdown
Copy
Edit
user-api-refactored/
├── user_api_refactored/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   ├── init_db.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── requirements.txt
└── README.md
💡 Notes
Make sure you activate the virtual environment before running the app.

Database path is fixed using os.path.abspath() to avoid misalignment.

Sample data includes 3 default users after running init_db.py.

💻 Developed With
Python 3.11+

Flask 2.3.2

Werkzeug 2.3.6

SQLite3 (built-in with Python)

Happy coding! ⚡

