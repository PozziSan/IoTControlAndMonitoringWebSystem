from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('turn_led_on', views.turn_led_on, name="turn_led_on")
]