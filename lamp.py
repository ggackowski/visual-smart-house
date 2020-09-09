from device import Device

class Lamp(Device): 
    def __init__(self, id, x, y, state, visualizer, room):
        Device.__init__(self, id, x, y, state, visualizer, room)
        
    def draw(self, chunk_size):
        if self._room == self._visualizer.get_room():
            self.chunk_size = chunk_size
            if self._state == 'on':
                self.draw_circle(chunk_size, chunk_size / 3, fill="yellow", outline="yellow", width=4)
            else:
                self.draw_circle(chunk_size, chunk_size / 3, fill="white", outline="gray", width=4)


    def execute(self, command):
        if command == 'on':
            self._state = 'on'
        elif command == 'off':
            self._state = 'off'
        self.draw(self.chunk_size)
        self._visualizer._window.update()