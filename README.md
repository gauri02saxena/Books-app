# 📚 Books App with CRUD APIs and JWT Authentication – Django REST Framework

This is a backend REST API for a simple **Books Application** built using **Python** and **Django REST Framework**. It supports user registration, JWT-based authentication, and full CRUD operations for managing books.

---

## 🚀 Features

### ✅ User Authentication
- Register a new user
- Login to receive a JWT token
- JWT used for secure session management
- Passwords are securely hashed

### 📝 CRUD Operations for Books (Authenticated)
- Create new books (single or multiple)
- Read list of all books
- Update entire book (PUT)
- Partial update (PATCH) of book fields
- Delete a book

### 🔒 Security
- JWT authentication protects all book endpoints
- Passwords stored securely (hashed)
- Sensitive data handled using `.env`

---

## 🧪 API Endpoints

### 🔐 Authentication

| Method | Endpoint             | Description         |
|--------|----------------------|---------------------|
| POST   | `/auth/register/`    | Register a user     |
| POST   | `/auth/login/`       | Get JWT token pair  |

### 📚 Books (Requires JWT Token)

| Method | Endpoint                      | Description                  |
|--------|-------------------------------|------------------------------|
| GET    | `/books/`                     | Get all books                |
| POST   | `/books/create`               | Add one or more books        |
| PUT    | `/books/update/<id>/`         | Full update a book by ID     |
| PATCH  | `/books/partial-update/<id>/` | Partially update book by ID  |
| DELETE | `/books/delete/<id>/`         | Delete a book by ID          |

---


