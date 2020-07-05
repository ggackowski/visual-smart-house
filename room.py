class Room:
    def __init__(self, name, x, y, visualizer):
        self._name = name
        self._x = x
        self._y = y
        self._visualizer = visualizer
        self._elements = []

    def getWidth(self):
        return self._x
    
    def getHeight(self):
        return self._y

    def getElementById(self, id):
        for element in self._elements:
            if element._id == id:
                return element    
    
    def getName(self):
        return self._name
    
    def addElement(self, element):
        self._elements.append(element)

    def draw(self):
        self._visualizer.set_room(self._name)
        self._visualizer.create_canvas()
        chunk_size = 1
        if self._x > self._y:
            chunk_size = self._visualizer._roomview_width // self._x
        else: 
            chunk_size = self._visualizer._height // self._y

        self._visualizer._canvas.create_rectangle((0, 0, chunk_size*self._x, chunk_size*self._y), fill='#ffffff', width=1)
        for element in self._elements:
            element.draw(chunk_size)

        