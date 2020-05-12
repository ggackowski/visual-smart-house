from data_provider import load_rooms_data_from_json
from visualizer import Visualizer
import tkinter as tk

def main():
    rooms = load_rooms_data_from_json('/data/default.json') 
    visualizer = Visualizer('Visual Smart House', 500, 500)

    for room in rooms:
        visualizer.draw(room)

    visualizer.main_loop()

if __name__ == '__main__':
    main()
