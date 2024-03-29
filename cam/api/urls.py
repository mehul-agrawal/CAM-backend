# File created at 2024-03-29 16:14:49 UTCfrom django.urls import include, path
from rest_framework_nested import routers

router = routers.SimpleRouter()

urlpatterns = [
	path('', include(router.urls))
]
