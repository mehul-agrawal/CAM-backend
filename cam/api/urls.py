from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'assignments', views.AssignmentView, basename='assignment')
router.register(r'marks', views.MarksView, basename='mark')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
