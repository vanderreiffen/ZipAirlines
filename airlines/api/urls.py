from django.urls import path, include
from .views import AirCraftAPIView
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aircraft', AirCraftAPIView)

urlpatterns = [
    url(r'', include(router.urls), name='aircraft-api')
]

app_name = 'airlines'
