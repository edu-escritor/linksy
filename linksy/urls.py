from django.contrib import admin
from django.urls import path

from api.views.auth.login_view import LoginView
from api.views.auth.refresh_view import RefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/auth/login/",
        LoginView.as_view(),
        name="auth_login",
    ),
    path(
        "api/auth/refresh/",
        RefreshView.as_view(),
        name="auth_refresh",
    ),
]
