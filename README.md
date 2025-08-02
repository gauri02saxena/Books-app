# 📚 Books & Authors API – A Django REST Framework Project
A robust RESTful API built using **Django REST Framework**, supporting full CRUD operations for **Books** and **Authors**, secure **JWT authentication**, and both **basic and advanced nested filtering** with GET/POST methods.

---

## 🚀 Features

### 🔐 User Authentication
- JWT-based secure login system.
- Register users via `POST /auth/register/`
- Obtain access/refresh token via `POST /auth/login/`
- Secure token refresh via `POST /auth/token/refresh/`
- Passwords are securely hashed using Django's built-in user model.

### 📖 CRUD for Books & Authors
- Create, list, update, delete Books and Authors.
- Bulk book creation supported.
- `ModelViewSet` based implementation for scalable code.
- Auth-protected views using `IsAuthenticated`.

### 🔍 Filtering Support
#### ✅ GET (Basic Field Filtering)
Supports standard field-based filters:
- `/books/?title__icontains=python`
- `/books/?pages__gt=200`
- `/books/?author__city=Delhi`

#### ✅ POST (Dynamic Complex Filtering)
Supports unlimited levels of nested filtering logic:
```json
{
  "operator": "and",
  "children": [
    { "field": "title", "op": "icontains", "value": "django" },
    {
      "operator": "or",
      "children": [
        { "field": "pages", "op": "gt", "value": 100 },
        { "field": "author__city", "op": "iexact", "value": "Delhi" }
      ]
    }
  ]
}
```
## 🧰 Tech Stack

- **Backend**: Python, Django, Django REST Framework  
- **Auth**: JWT (via `SimpleJWT`)  
- **Filtering**: `django-filter`, dynamic `Q`-objects  
- **Testing**: Postman  
- **Security**: `.env` via `python-decouple`, JWT, password hashing  

---

## 📫 API Endpoints

### 🔐 Authentication

| Method | Endpoint                 | Description         |
|--------|--------------------------|---------------------|
| POST   | `/auth/register/`        | Register user       |
| POST   | `/auth/login/`           | Get JWT token pair  |
| POST   | `/auth/token/refresh/`   | Refresh JWT token   |

---

### 📚 Book Management (Requires Token)

| Method | Endpoint              | Description               |
|--------|-----------------------|---------------------------|
| GET    | `/books/`             | List all books            |
| POST   | `/books/`             | Create one or more books  |
| PUT    | `/books/<id>/`        | Update full book details  |
| PATCH  | `/books/<id>/`        | Partially update book     |
| DELETE | `/books/<id>/`        | Delete a book             |
| GET    | `/books/?title=xyz`   | Filter via query params   |
| POST   | `/books/filter/`      | Apply nested filters      |

---

### 👨‍💼 Author Management (Requires Token)

| Method | Endpoint              | Description        |
|--------|-----------------------|--------------------|
| GET    | `/authors/`           | List all authors   |
| POST   | `/authors/`           | Create an author   |
| PUT    | `/authors/<id>/`      | Update author      |
| DELETE | `/authors/<id>/`      | Delete author      |

---

## 📸 Postman Testing

All endpoints have been tested and validated using Postman.

🖼️ A few key screenshots of successful test responses are included below from the `/testing-snapshots/` folder:

### 🔐 1. JWT Login (POST `/auth/login/`)
![User Login](testing-snapshots/user_login.png)

### 📘 2. List All Books (GET `/books/`)
![List All Books](testing-snapshots/list_all_books.png)

### 🔎 3. Query Params Filtering (GET `/books/?title__icontains=python`)
![Query Params Filtering](testing-snapshots/query_params_filtering.png)

### ✅ 4. Dynamic Nested Filtering (POST `/books/filter/`)
![Dynamic Nested Filtering](testing-snapshots/dynamic_nested_filtering.png)


---

## 📂 Project Structure Highlights

```
myapp/
├── models.py            # Book and Author models
├── serializers.py       # DRF serializers
├── views/
│   ├── crud.py          # CRUD operations using ViewSets
│   ├── auth.py          # RegisterView (JWT auth)
│   └── filters.py       # Dynamic nested filter + basic query param logic
├── urls.py              # All route definitions
```

---

## ✅ Standards & Best Practices

- ✅ Uses `ViewSets` for clean, DRY CRUD implementation.
- ✅ Logging added for key actions (create, update, register).
- ✅ Modular views (auth, filters, crud separated).
- ✅ Strong comments in Python docstrings for clarity.
- ✅ JWT-based secure authentication & session handling.
- ✅ Uses `.env` and `decouple` for config separation.
- ✅ Validated against standard REST API design practices.

---

## 🧪 Sample Test Queries

### 🔎 Basic GET Query Params:

- `/books/?title__icontains=python`
- `/books/?pages__gt=200`
- `/books/?author__city=Delhi`

### 🔍 POST Dynamic Filtering:

```json
{
  "operator": "and",
  "children": [
    {
      "field": "title",
      "op": "icontains",
      "value": "django"
    },
    {
      "operator": "or",
      "children": [
        {
          "operator": "and",
          "children": [
            { "field": "pages", "op": "gt", "value": 100 },
            { "field": "author__city", "op": "iexact", "value": "Delhi" }
          ]
        },
        {
          "operator": "and",
          "children": [
            { "field": "pages", "op": "lt", "value": 300 },
            { "field": "author__city", "op": "iexact", "value": "Bangalore" }
          ]
        }
      ]
    }
  ]
}

```

---

## 📛 Error Handling

- `400 Bad Request`: Invalid filters or payloads  
- `401 Unauthorized`: Missing or invalid token  
- `404 Not Found`: Book or Author not found  

---

## 🧠 Author

**Gauri Saxena**  
[LinkedIn](https://www.linkedin.com/in/gaurisaxena02/) • [GitHub](https://github.com/gauri02saxena) • gaurisaxena7379@gmail.com


