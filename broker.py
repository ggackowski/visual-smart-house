import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.payload)

class Broker:
    def __init__(self, where, port):
        self._topics = []
        self._client = mqtt.Client()
        self._where = where
        self._port = port

    def add_topic(self, topic):
        self._topics.append(topic)

    def start(self):
        self._client.on_message = on_message
        self._client.connect(self._where, self._port, 60)
        for topic in self._topics:
            self._client.subscribe(topic)
        self._client.loop_forever()

broker = Broker('localhost', 1883)
broker.add_topic('ok')
broker.start()
