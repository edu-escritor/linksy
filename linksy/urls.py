from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views.auth.login_view import LoginView
from api.views.auth.refresh_view import RefreshView
from api.views.page_view_set import PageViewSet

router = SimpleRouter()

router.register(
    "pages",
    PageViewSet,
    basename="page",
)


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
    path(
        "api/",
        include(router.urls),
    ),
]
