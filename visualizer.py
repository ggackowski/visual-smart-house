import tkinter as tk

class Visualizer:
    def __init__(self, title, w, h):
        self._window = tk.Tk()
        self._window.title(title)
        self._window.geometry('{0}x{1}'.format(w, h))
        self._canvas = tk.Canvas(self._window, width=w, height=w)
        self._canvas.place(x=1,y=1)
    
    def draw(self, element):
        if type(element).__name__ == 'Room':
            self._canvas.create_rectangle((0, 0, 10*element._x, 10*element._y), fill='#ffffff', width=1)
            for element in element._elements:
                if type(element).__name__ == 'Window':
                    self._canvas.create_rectangle((10*element._x, 10*element._y, 10* element._x + 10, 10*element._y + 10), fill='#0000ff', width=1)
                elif type(element).__name__ == 'Lamp':
                     self._canvas.create_rectangle((10*element._x, 10*element._y, 10* element._x + 10, 10*element._y + 10), fill='#ff0000', width=1)

    def main_loop(self):
        self._window.mainloop()