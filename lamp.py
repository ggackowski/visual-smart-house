from device import Device

class Lamp(Device): 
    def __init__(self, id, x, y, state, visualizer, room):
        Device.__init__(self, id, x, y, state, visualizer, room)
        
    def draw(self, chunk_size):
        if self._room == self._visualizer.get_room():
            self.chunk_size = chunk_size
            if self._state == 'on':
                self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#ffff00', width=1)
            else:
                self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#ffffff', width=1)


    def execute(self, command):
        if command == 'on':
            self._state = 'on'
        elif command == 'off':
            self._state = 'off'
        self.draw(self.chunk_size)
        self._visualizer._window.update()