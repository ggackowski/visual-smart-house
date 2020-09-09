from device import Device

class Window(Device):
    def __init__(self, id, x, y, state, visualizer, room):
        Device.__init__(self, id, x, y, state, visualizer, room)

    def draw(self, chunk_size):
        if self._room == self._visualizer.get_room():
            self.chunk_size = chunk_size
            if self._state == 'open':
                self.draw_circle(chunk_size, chunk_size / 2, fill="white", outline="blue", width=4)
            elif self._state == 'close':
                self.draw_circle(chunk_size, chunk_size / 2, fill="blue", outline="blue", width=4)

    def execute(self, command):
        if command == 'open':
            self._state = 'open'
        elif command == 'close':
            self._state = 'close'
        self.draw(self.chunk_size)
        self._visualizer._window.update()