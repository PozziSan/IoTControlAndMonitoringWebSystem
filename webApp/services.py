import paho.mqtt.client as mqtt
from functools import lru_cache


class Mqtt():
    def __init__(self):
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.loop_started = False
        self.connected = False

        print('teste')

    def on_connect(self):
        print('Connected!')
        self.client.subscribe('aaaa')

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def get_client(self):
        return self.client

    def connect(self, connection_address, a, b):
        if self.connected:
            return
        else:
            self.client.coonect(connection_address, a, b)
            self.connected = True

    def start_loop(self):
        if self.loop_started:
            return
        else:
            self.client.loop_start()
            self.loop_started = True


@lru_cache(maxsize=None)
def get_mqtt():
    return Mqtt()
