from data_provider import load_rooms_data_from_json
from visualizer import Visualizer
from controller import Controller
import paho.mqtt.client as mqtt
import tkinter as tk
import time

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
    client.connect('localhost', 1883, 60)
    client.subscribe('ok')
    client.loop_start()


def main():
    visualizer = Visualizer('Visual Smart House', 640, 480)
    global rooms
    rooms = load_rooms_data_from_json('/data/default.json', visualizer) 

    controller = Controller(rooms, visualizer)

    run_mqtt()

    visualizer.main_loop()

if __name__ == '__main__':
    main()
