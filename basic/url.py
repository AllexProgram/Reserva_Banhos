from django.urls import path
from rest_framework import routers
from basic.views import reserva


app_name = "reserva"

router = routers.SimpleRouter()

urlpatterns = [path("reserve", reserva)]

urlpatterns = urlpatterns + router.urls

