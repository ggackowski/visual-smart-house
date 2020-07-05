class Device:
    def __init__(self, id, x, y, state, visualizer, room):
        self._id = id
        self._x = x
        self._y = y
        self._visualizer = visualizer
        self._state = state
        self._room = room

