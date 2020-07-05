from device import Device
import threading
import time

class MotionSensor(Device): 
    def __init__(self, id, x, y, state, visualizer, room):
        Device.__init__(self, id, x, y, state, visualizer, room)
        
    def draw(self, chunk_size):
        if self._room == self._visualizer.get_room():
            self.chunk_size = chunk_size
            if self._state == 'movement':
                self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#000000', width=1)
            else:
                self._visualizer._canvas.create_rectangle((chunk_size*self._x, chunk_size*self._y, chunk_size* self._x + chunk_size, chunk_size*self._y + chunk_size), fill='#ffffff', width=1)

    def indicate_movement(self):
        print('tez ok')
        time.sleep(5)
        self.execute('off')

    def execute(self, command):
        if command == 'movement':
            print('ok')
            self._state = 'movement'
            thread = threading.Thread(target = self.indicate_movement)
            thread.start()
        elif command == 'off':
            self._state = 'off'
        self.draw(self.chunk_size)
        self._visualizer._window.update()