from rest_framework import routers
from todos import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
