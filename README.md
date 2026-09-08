# 🔗 Linksy

**Linksy** is a web application for organising and managing links in a structured way.

The project is being developed primarily as a **learning project**, with the goal of gaining practical experience with
Python, Django, PostgreSQL and API development.

## 🎯 Purpose

Linksy works as a personal link aggregator.

Links can be organised using:

* **Pages**, which represent the main sections of the application.
* **Tags**, which can be displayed on multiple pages.
* **Links**, which can belong to multiple tags.

This allows the same link to appear in different contexts without being duplicated.

For example, a Gmail link could belong to both the `Email` and `Personal` tags, while the `Email` tag itself could
appear on several pages.

Pages, tags and links support manual ordering so that their position can be controlled independently.

## 🧱 Stack

The backend is built using:

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL**
* **Vue.Js**

The project is intended to provide practical experience with:

* REST API development
* Django models and ORM
* relational database modelling
* many-to-many relationships
* migrations
* validation
* testing
* authentication and user management at a later stage

## 🗃️ Data Model

The main entities are:

```text
User
Page
Tag
Link
PageTag
LinkTag
```

The main relationships are:

```text
User 1 ─── N Page
User 1 ─── N Tag
User 1 ─── N Link

Page N ─── N Tag
Tag  N ─── N Link
```

`PageTag` stores the position of a tag within a page.

`LinkTag` stores the position of a link within a tag.

This means that the same tag can appear on several pages and the same link can belong to several tags.

## 👤 Users

User authentication is not part of the initial implementation.

The data model is nevertheless designed with multiple users in mind. During the first development stage, all data will
belong to a predefined default user.

Authentication and user management can therefore be added later without requiring a major redesign of the database
structure.

## 🐘 PostgreSQL

To configure PostgreSQL to use fewer resources during development, edit:

```text
/etc/postgresql/16/main/postgresql.conf
```

Change the following values:

```ini
shared_buffers = 64MB
max_connections = 20
work_mem = 2MB
maintenance_work_mem = 32MB
```

Restart the service:

```bash
sudo systemctl restart postgresql
```

## 🖥️ PostgreSQL Client

To use the PostgreSQL client as administrator:

```bash
sudo -u postgres psql
```

To connect using the Linksy development user:

```bash
psql -h localhost -U linksy_dev -d linksy
```

## 🚦 Status

Linksy is currently under development.

Its main purpose is learning, so the architecture, data model and features may change as the project evolves.

# 🔗 API URLs

For more information about the routes, check [URLs](URLS.md)