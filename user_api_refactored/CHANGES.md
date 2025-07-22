
# 🛠️ CHANGES.md

## 🔧 Project: User Management API (Legacy Flask Code Refactor)
**Author:** Darshan Kumar  
**Date:** July 22, 2025    
**Purpose:** Code cleanup, stability, modularization, bug fixes, and documentation

---

## 🔍 Major Issues Identified


## 🧩 1. Code Organization
✅ Proper Separation of Concerns
Refactored the monolithic app.py into clearly organized layers:

routes/ for HTTP endpoints

services/ for business logic

models/ for database interactions

utils/ for validations

This modular structure ensures better readability, testability, and future scalability.

✅ Clear Project Structure
Introduced a proper Python package using __init__.py

Final directory layout follows conventional best practices:

Copy
Edit
user_api_refactored/
├── app.py
├── db.py
├── init_db.py
├── routes/
├── services/
├── models/
└── utils/
✅ Justification:
Follows the Separation of Concerns (SoC) principle

Easier to maintain, test, and scale the codebase

Aligns with industry practices for Flask-based REST APIs

⚖️ Trade-off:
Slight increase in file complexity, but long-term maintainability improved drastically


## 🔐 2. Security Improvements 
✅ Fixed SQL Injection Vulnerabilities
Replaced all raw SQL string concatenation with parameterized queries:

python
Copy
Edit
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
✅ Implemented Input Validation
Added custom validation logic using utils/validation.py

Required fields (name, email, password) are checked before DB operations

Invalid or missing fields return 400 Bad Request

✅ Protected Sensitive Logic
Centralized database access via get_db_connection() for uniform DB security and error control

Prevented crashes by wrapping logic in try-except blocks in all POST endpoints
✅ Justification:
Prevents SQL injection attacks

Ensures only clean data reaches the database

Makes DB access predictable and debuggable

⚖️ Trade-off:
Slight verbosity and extra function calls, but significant security gain

## ⚙️ 3. Best Practices 
✅ Robust Error Handling
All service-level functions now handle runtime exceptions:

python
Copy
Edit
try:
    ...
except Exception as e:
    return jsonify({"error": str(e)}), 500
✅ Correct HTTP Status Codes
Used appropriate status codes:

200 OK for successful GETs

201 Created on successful POST

400 Bad Request for validation errors

401 Unauthorized for failed login

500 Internal Server Error for unknown issues

✅ Code Reusability
Separated reusable logic like:

DB connection

Input validation

Encourages future scalability and unit testing


## 🤖 Use of AI Tools

### Tools Used:
- ChatGPT (OpenAI GPT-4)

### Purpose:
- Assisted in initial debugging and resolving configuration issues during:
  - **SQLite database path handling**
  - **Clarifying `__init__.py` usage and Python package imports**


### Level of Use:
- AI assistance was used **strictly as a support tool** (approx. 10% of the work)
- All architectural design, refactoring, routing logic, and validation code were implemented and verified by me

### Edits and Oversight:
- All AI-suggested code and markdown outputs were:
  - Reviewed and manually edited to fit the project structure
  - Modified to maintain consistency with existing naming conventions and logic
  - Rejected or rewritten when misaligned with the project scope or requirements

This project reflects my direct understanding of Flask backend development, with limited AI usage as a debugging and productivity enhancer — not as a replacement for development ownership.
