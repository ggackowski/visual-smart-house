import tkinter as tk

class Visualizer:
    def __init__(self, title, w, h):
        self._window = tk.Tk()
        self._window.title(title)
        self._window.geometry('{0}x{1}'.format(w, h))
        self._canvas = tk.Canvas(self._window, width=w, height=w)
        self._canvas.place(x=1,y=1)
    
    def draw(self, element):
        pass

    def main_loop(self):
        self._window.mainloop()