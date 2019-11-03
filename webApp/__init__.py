from .services import get_mqtt

mqtt = get_mqtt()

mqtt.connect('192.168.0.104')
#
# mqtt.connect()
mqtt.start_loop()