import json
from room import Room
from lamp import Lamp
from window import Window
from motion_sensor import MotionSensor
from visualizer import Visualizer

def load_rooms_data_from_json(file, vis):
    with open('data/default.json', 'r') as f:
        data_dict = json.load(f)

    rooms = {}

    for r in data_dict['plan']:
        rm = data_dict['plan'][r]
        room = Room(r, rm['width'], rm['height'], vis)
        for elm in rm['elements']:

            if elm['type'] == 'lamp':
                lamp = Lamp(elm['id'], elm['position']['x'], elm['position']['y'], 'on', vis, r)
                room.addElement(lamp)

            elif elm['type'] == 'window':
                window = Window(elm['id'], elm['position']['x'], elm['position']['y'], 'close', vis, r)    
                room.addElement(window)

            elif elm['type'] == 'motion_sensor':
                motion_sensor = MotionSensor(elm['id'], elm['position']['x'], elm['position']['y'], 'off', vis, r)    
                room.addElement(motion_sensor)

        rooms[room.getName()] = room
    
    return rooms
