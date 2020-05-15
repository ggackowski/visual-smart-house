from data_provider import load_rooms_data_from_json
from visualizer import Visualizer
import tkinter as tk

def main():
    visualizer = Visualizer('Visual Smart House', 500, 500)
    rooms = load_rooms_data_from_json('/data/default.json', visualizer) 

    rooms[0].getElementById(1).turnOff()

    for room in rooms:
        room.draw()

    visualizer.main_loop()

if __name__ == '__main__':
    main()
