from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from .services import get_mqtt

from .models import TemperatureMeasures
from .models import HumidityMeasures


# Create your views here.
def index(request):
    return render(request, 'webApp/index.html')


def turn_led_on(request):
    mqtt = get_mqtt()

    mqtt.publish_message('webApp/actuator', '1')

    return HttpResponse(status=200)


def temperature_measures(request):
    temperature_measures_list = TemperatureMeasures.objects.all().order_by('-created_at')

    paginator = Paginator(temperature_measures_list, 30)
    page = request.GET.get('page')
    measures = paginator.get_page(page)

    return render(request, 'webApp/temperature_measures.html', {'temperature_measures': measures})


def humidity_measures(request):
    humidity_measures_list = HumidityMeasures.objects.all().order_by('-created_at')

    paginator = Paginator(humidity_measures_list, 30)
    page = request.GET.get('page')
    measures = paginator.get_page(page)

    return render(request, 'webApp/humidity_measures.html', {'humidity_measures': measures})
