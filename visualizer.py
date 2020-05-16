import tkinter as tk

class Visualizer:
    def __init__(self, title, w, h):
        self._window = tk.Tk()
        self._window.title(title)
        self._window.geometry('{0}x{1}'.format(w, h))
        self._width = w
        self._height = h
        self.create_canvas()
        self._room_buttons = []
    
    def create_canvas(self):
        self._canvas = tk.Canvas(self._window, width=self._width - 400, height=self._height)
        self._canvas.place(x=0,y=0)

    def add_buttons(self, rooms):
        for name in rooms:
            room = rooms[name]
            button = tk.Button(self._window, text=room._name, command=room.draw)
            self._room_buttons.append(button)
            button.pack()


    def main_loop(self):
        self._window.mainloop()