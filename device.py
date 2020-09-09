class Device:
    def __init__(self, id, x, y, state, visualizer, room):
        self._id = id
        self._x = x
        self._y = y
        self._visualizer = visualizer
        self._state = state
        self._room = room
    
    def draw_circle(self, chunk_size, r, **kwargs):
        self._visualizer.create_circle(chunk_size * self._x + r, chunk_size * self._y + r, r, **kwargs)


