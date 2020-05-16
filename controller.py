

class Controller:
    def __init__(self, rooms, visualizer):
        self._rooms = rooms
        self._visualizer = visualizer
        self._visualizer.add_buttons(self._rooms)
        self._rooms['kitchen'].draw()
        
        
