from device import Device

class Window(Device):
    def __init__(self, id, x, y, state, visualizer):
        Device.__init__(self, id, x, y, state, visualizer)

    def draw(self, chunk_size):
        self.chunk_size = chunk_size
        if self._state == 'open':
            self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#0000ff', width=1)
        elif self._state == 'close':
            self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#00f0ff', width=1)

    def execute(self, command):
        if command == 'open':
            self._state = 'open'
        elif command == 'close':
            self._state = 'close'
        self.draw(self.chunk_size)
        self._visualizer._window.update()