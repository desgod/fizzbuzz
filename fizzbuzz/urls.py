from django.conf.urls import url, include
from rest_framework import routers
from fizzbuzz.api import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'fizzbuzz', views.FizzBuzzViewSet, base_name='fizzbuzz')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
