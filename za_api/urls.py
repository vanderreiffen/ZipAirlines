from django.urls import include,path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('airplane', views.AirplaneViewSet)

# urlpatterns = [
#     # path('api/', include(router.urls)),
#     url(r'api/', include((router.urls, 'za_api'),namespace='airplane-api')),
#     # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    url(r'^api/', include((router.urls, 'za_api'), namespace='airline-api')),
]