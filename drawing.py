class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Line:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas, color="black"):
        canvas.create_line(
            self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=color, width=2
        )


class Cell:
    def __init__(self, point, width, height):
        self.width = width
        self.height = height
        self._x1, self._y1 = point.x, point.y
        self._x2, self._y2 = point.x + self.width, point.y + self.height
        self.top_wall = True
        self.bot_wall = True
        self.left_wall = True
        self.right_wall = True
        self.visited = False

    def draw(self, window, color, bg_color):
        if window is None:
            return
        if self.top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            window.draw_line(line, color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            window.draw_line(line, bg_color)

        if self.bot_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            window.draw_line(line, color)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            window.draw_line(line, bg_color)

        if self.left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            window.draw_line(line, color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            window.draw_line(line, bg_color)

        if self.right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            window.draw_line(line, color)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            window.draw_line(line, bg_color)

    def draw_move(self, window, to_cell, undo=False):
        if undo:
            color = "red"
        else:
            color = "gray"
        cen_p1 = Point(self._x1 + (self.width / 2), self._y1 + (self.height / 2))
        cen_p2 = Point(
            to_cell._x1 + (to_cell.width / 2), to_cell._y1 + (to_cell.height / 2)
        )
        window.draw_line(Line(cen_p1, cen_p2), color)
