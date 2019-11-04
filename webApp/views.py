from django.shortcuts import render
from .services import get_mqtt
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'webApp/index.html')


def turn_led_on(request):
    mqtt = get_mqtt()

    mqtt.publish_message('webApp/actuator', '1')

    return HttpResponse(status=200)
