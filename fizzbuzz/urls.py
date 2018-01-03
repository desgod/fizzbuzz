from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from fizzbuzz.api import views


router = routers.DefaultRouter()
router.register(r'fizzbuzz', views.FizzBuzzViewSet, base_name='fizzbuzz')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
