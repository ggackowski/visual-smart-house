import tkinter as tk

class Visualizer:
    def __init__(self, title, w, h):
        self._window = tk.Tk()
        self._window.title(title)
        self._window.geometry('{0}x{1}'.format(w, h))
        self._width = w
        self._height = h
        self._roomview_width = self._width - 200
        self.create_canvas()
        self._room = ''
        self._room_buttons = []
        self._buttons = tk.LabelFrame(self._window, text="Rooms")
        self._buttons.place(x=self._roomview_width + 10, y=0)

    def create_canvas(self):
        self._canvas = tk.Canvas(self._window, width=self._roomview_width, height=self._height)
        self._canvas.place(x=0,y=0)

    def add_buttons(self, rooms):
        for name in rooms:
            room = rooms[name]
            button = tk.Button(self._buttons, text=room._name, command=room.draw)
            self._room_buttons.append(button)
            button.pack()

    def set_room(self, room_name):
        self._room = room_name

    def get_room(self):
        return self._room

    def main_loop(self):
        self._window.mainloop()