import paho.mqtt.client as mqtt
from functools import lru_cache


class Mqtt():
    def __init__(self):
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.loop_started = False
        self.connected = False

    def on_connect(self):
        print('Connected!')
        self.client.subscribe('test_topic')

    def on_message(self, client, userdata, msg):
        print(f'{msg.topic} {str(msg.payload)}')

    def get_client(self):
        return self.client

    def publish_message(self, topic, message):
        if not self.connected:
            return

        self.client.publish(topic, message)

    def connect(self, connection_address):
        if self.connected:
            return

        self.client.connect(connection_address)
        self.connected = True

    def start_loop(self):
        if self.loop_started:
            return

        self.client.loop_start()
        self.loop_started = True


@lru_cache(maxsize=None)
def get_mqtt():
    return Mqtt()
