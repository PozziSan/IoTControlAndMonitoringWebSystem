from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('turn_led_on', views.turn_led_on, name="turn_led_on"),
    path('temperature_measures', views.temperature_measures, name='temperature_measures'),
    path('humidity_measures', views.humidity_measures, name='humidity_measures')
]