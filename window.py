from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, bg_color="white"):
        self._root = Tk()
        self._root.title("Window")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg=bg_color, width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False

    def draw_line(self, line, color):
        line.draw(self._canvas, color)

    def draw_cell(self, cell, cell_color, bg_color):
        cell.draw(self, cell_color, bg_color)

    def draw_move(self, cell, to_cell, undo=False):
        cell.draw_move(self, to_cell, undo)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def mainloop(self):
        self._root.mainloop()

    def close(self):
        self._root.quit()
