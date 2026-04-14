# AvtoShop Backend API

Production-oriented FastAPI backend for AvtoShop with persistent storage, JWT auth, admin-protected service mutations, validation, and consistent JSON errors.

## Features

- Persistent SQLite storage via SQLAlchemy (`DATABASE_URL` configurable)
- JWT bearer authentication for admin users
- Password hashing with Argon2
- Normalized API contract:
  - `POST /api/auth/login`
  - `POST /api/auth/logout`
  - `GET /api/services`
  - `POST /api/services` (admin)
  - `PUT /api/services/:id` (admin)
  - `DELETE /api/services/:id` (admin)
  - `GET /api/reviews`
  - `POST /api/reviews`
- Legacy compatibility aliases:
  - `GET /api/posts`
  - `POST /api/posts` (admin)
  - `PUT /api/post/:id` (admin)
  - `DELETE /api/post/:id` (admin)
- Unified error shape:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request validation failed",
    "details": []
  }
}
```

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy env template:
   - `cp .env.example .env`
4. Run API:
   - `uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload`

The app creates tables and seeds:
- one admin from `SEED_ADMIN_EMAIL` and `SEED_ADMIN_PASSWORD`
- optional sample services/reviews when `SEED_SAMPLE_DATA=true`

## Frontend integration notes

- Use `Authorization: Bearer <token>` for service create/update/delete.
- Prefer normalized `/api/services` routes in frontend.
- Legacy `/api/posts` and `/api/post/:id` are temporary migration aliases.

## Local API checks

Use `test_main.http` to run login, service CRUD, review submit/list, and validation error scenarios.
