# 🔗 API URLs

## 🔑 Tokens

### POST /api/auth/login/

Authenticates a user and returns access and refresh tokens.

* **Method:** `POST`
* **Route:** `/api/auth/login`
* **Name:** `auth_login`

#### Request

```json
{
  "username": "john_doe",
  "password": "0123456789"
}
```

#### Response

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### POST /api/auth/refresh/

Generates a new access token from a valid refresh token.

**Method:** `POST`
**Route:** `/api/auth/refresh`
**Name:** `auth_refresh`

#### Request

```json
{
  "refresh": "<refresh_token>"
}
```

#### Response

```json
{
  "access": "<access_token>"
}
```

## 📄 Pages

All page endpoints require authentication using an access token.

```http
Authorization: Bearer <access_token>
```

### GET /api/pages/

Returns all pages belonging to the authenticated user.

* **Method:** `GET`
* **Route:** `/api/pages`
* **Name:** `page-list`

#### Response

```json
[
  {
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Linksy",
    "color": "#ffffff",
    "position": 0
  }
]
```

### GET /api/pages/{uuid}/

Returns a specific page belonging to the authenticated user.

* **Method:** `GET`
* **Route:** `/api/pages/{uuid}`
* **Name:** `page-detail`

#### Response

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Linksy",
  "color": "#ffffff",
  "position": 0,
  "created_at": "2026-09-09T10:00:00Z",
  "updated_at": "2026-09-09T10:00:00Z"
}
```

### POST /api/pages/

Creates a new page for the authenticated user.

* **Method:** `POST`
* **Route:** `/api/pages`
* **Name:** `page-list`

#### Request

```json
{
  "title": "Work",
  "color": "#90dbf4",
  "position": 1
}
```

#### Response

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Work",
  "color": "#90dbf4",
  "position": 1,
  "created_at": "2026-09-09T10:00:00Z",
  "updated_at": "2026-09-09T10:00:00Z"
}
```

### PUT /api/pages/{uuid}

Replaces the data of a specific page belonging to the authenticated user.

* **Method:** `PUT`
* **Route:** `/api/pages/{uuid}`
* **Name:** `page-detail`

#### Request

```json
{
  "title": "Personal",
  "color": "#caffbf",
  "position": 2
}
```

#### Response

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Personal",
  "color": "#caffbf",
  "position": 2,
  "created_at": "2026-09-09T10:00:00Z",
  "updated_at": "2026-09-09T11:00:00Z"
}
```

### PATCH /api/pages/{uuid}

Partially updates a specific page belonging to the authenticated user.

* **Method:** `PATCH`
* **Route:** `/api/pages/{uuid}`
* **Name:** `page-detail`

#### Request

```json
{
  "title": "Personal"
}
```

#### Response

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Personal",
  "color": "#caffbf",
  "position": 2,
  "created_at": "2026-09-09T10:00:00Z",
  "updated_at": "2026-09-09T11:00:00Z"
}
```

### DELETE /api/pages/{uuid}

Deletes a specific page belonging to the authenticated user.

The user's last remaining page cannot be deleted.

* **Method:** `DELETE`
* **Route:** `/api/pages/{uuid}`
* **Name:** `page-detail`

#### Response

```text
204 No Content
```
