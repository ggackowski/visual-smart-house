from data_provider import load_rooms_data_from_json
from visualizer import Visualizer
from controller import Controller
import paho.mqtt.client as mqtt
import tkinter as tk
import time
import sys

rooms = {}

def parse_message(msg):
    msg = msg[2:-1]
    w = msg.split('/')
    rooms[w[0]].getElementById(w[1]).execute(w[2])

def on_message(client, userdata, msg):
    print(msg.payload)
    parse_message(str(msg.payload))

def run_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_host, mqtt_port, 60)
    client.subscribe(mqtt_topic)
    client.loop_start()


def main(argv):

    global config_filepath
    global mqtt_host
    global mqtt_port
    global mqtt_topic

    try:    
        with open('.vsh_config') as config:
            lines = config.read().splitlines()
            config_filepath = lines[0]
            mqtt_host = lines[1]
            mqtt_port = int(lines[2])
            mqtt_topic = lines[3]
    except EnvironmentError:
        config_filepath = 'data/default.json'
        mqtt_host = 'localhost'
        mqtt_port = 1883
        mqtt_topic = 'ok'

    visualizer = Visualizer('Visual Smart House', 640, 480)
    global rooms
    rooms = load_rooms_data_from_json(config_filepath, visualizer) 

    controller = Controller(rooms, visualizer)

    run_mqtt() 

    visualizer.main_loop()

if __name__ == '__main__':
    main(sys.argv)
