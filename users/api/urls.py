# File created at 2022-03-02 14:45:52 UTC

from django.urls import path
from users.api import views


urlpatterns = [
    path('', views.UserGetUpdateView.as_view())
]
