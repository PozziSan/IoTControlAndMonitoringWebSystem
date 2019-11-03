from django.apps import AppConfig


class WebappConfig(AppConfig):
    name = 'webApp'

    def ready(self):
        from webApp.services import get_mqtt

        mqtt = get_mqtt()

        mqtt.connect('192.168.0.104')
        mqtt.start_loop()
