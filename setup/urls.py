from django.contrib import admin
from django.urls import path, include
from apps.tutores.views import TutoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tutores', TutoresViewSet, basename='Tutores')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

