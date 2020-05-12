class Room:
    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y
        self._elements = []

    def getWidth(self):
        return self._x
    
    def getHeight(self):
        return self._y
    
    def getName(self):
        return self._name
    
    def addElement(self, element):
        self._elements.append(element)

