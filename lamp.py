from device import Device

class Lamp(Device): 
    def __init__(self, id, x, y, state, visualizer):
        Device.__init__(self, id, x, y, state, visualizer)

    def draw(self):
        if self._state == 'ok':
            self._visualizer._canvas.create_rectangle((10*self._x, 10*self._y, 10* self._x + 10, 10*self._y + 10), fill='#ffff00', width=1)
        else:
            self._visualizer._canvas.create_rectangle((10*self._x, 10*self._y, 10* self._x + 10, 10*self._y + 10), fill='#ffffff', width=1)

    def turnOn(self):
        self._state = 'ok'

    def turnOff(self):
        self._state = 'off'