# File created at 2022-03-08 06:26:18 UTC

from authentication.api import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view())
]
