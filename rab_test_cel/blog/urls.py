from django.urls import include, path
from rab_test_cel.online_account.views import PublishMessage

urlpatterns = [
    path("open/", PublishMessage.as_view(), name="publish_message"),
]