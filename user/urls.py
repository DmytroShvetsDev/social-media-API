from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from user.views import RegisterView, ManageUserView, RetrieveUserView, ListUsersView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("<int:pk>/", RetrieveUserView.as_view(), name="retrieve"),
    path("users/", ListUsersView.as_view(), name="users_list"),

]

app_name = "user"
