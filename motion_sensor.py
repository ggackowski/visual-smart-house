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
                self.draw_circle(chunk_size, chunk_size / 4, fill="red", outline="red", width=4)
            else:
                self.draw_circle(chunk_size, chunk_size / 4, fill="white", outline="red", width=4)

    def indicate_movement(self):
        time.sleep(5)
        self.execute('off')

    def execute(self, command):
        if command == 'movement':
            self._state = 'movement'
            thread = threading.Thread(target = self.indicate_movement)
            thread.start()
        elif command == 'off':
            self._state = 'off'
        self.draw(self.chunk_size)
        self._visualizer._window.update()