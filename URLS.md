# 🔗 API URLs

## 🔑 Tokens

### POST /api/auth/login/

Authenticates a user and returns access and refresh tokens.

* **Method:** `POST`
* **Route:** `/api/auth/login/`
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
**Route:** `/api/auth/refresh/`
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
