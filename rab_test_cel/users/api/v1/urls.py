from django.urls import path
from rab_test_cel.users.api.v1.views import UserCreateAPIView
app_name = "users_api_v1"
urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
