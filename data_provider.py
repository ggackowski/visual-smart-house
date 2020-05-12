import json
from room import Room
from lamp import Lamp
from window import Window

def load_rooms_data_from_json(file):
    with open('data/default.json', 'r') as f:
        data_dict = json.load(f)

    rooms = []

    for r in data_dict['plan']:
        rm = data_dict['plan'][r]
        room = Room(r, rm['width'], rm['height'])
        for elm in rm['elements']:

            if elm['type'] == 'lamp':
                lamp = Lamp(elm['id'], elm['position']['x'], elm['position']['y'])
                room.addElement(lamp)

            elif elm['type'] == 'window':
                window = Window(elm['id'], elm['position']['x'], elm['position']['y'])    
                room.addElement(window)
        rooms.append(room)
    
    return rooms
