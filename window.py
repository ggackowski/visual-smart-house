from device import Device

class Window(Device):
    def __init__(self, id, x, y, state, visualizer):
        Device.__init__(self, id, x, y, state, visualizer)

    def draw(self):
        self._visualizer._canvas.create_rectangle((10*self._x, 10*self._y, 10* self._x + 10, 10*self._y + 10), fill='#0000ff', width=1)