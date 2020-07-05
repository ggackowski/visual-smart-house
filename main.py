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

    if len(sys.argv) < 5:
        print("Not enough arguments!")
        print("python3 main.py <json config file> <mqtt host> <mqtt port> <mqtt topic>")
        exit()

    global config_filepath
    global mqtt_host
    global mqtt_port
    global mqtt_topic
    
    config_filepath = sys.argv[1]
    mqtt_host = sys.argv[2]
    mqtt_port = int(sys.argv[3])
    mqtt_topic = sys.argv[4]

    visualizer = Visualizer('Visual Smart House', 640, 480)
    global rooms
    rooms = load_rooms_data_from_json(config_filepath, visualizer) 

    controller = Controller(rooms, visualizer)

    run_mqtt()

    visualizer.main_loop()

if __name__ == '__main__':
    main(sys.argv)
