import time
import random
from drawing import Cell, Point


class Maze:
    def __init__(
        self,
        win,
        point,
        num_rows,
        num_cols,
        cell_width,
        cell_height,
        cell_color="black",
        bg_color="white",
        seed=None,
    ):
        self.win = win
        self.cell_color = cell_color
        self.bg_color = bg_color
        self._x1, self._y1 = point.x, point.y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self._cells = []
        self._create_cells()

        random.seed(seed)
        self._build_maze()
        self._reset_cells_visited()

    def _create_cells(self):
        for r in range(self.num_rows):
            cell_row = []
            for c in range(self.num_cols):
                coord = Point(
                    self._x1 + (self.cell_width * c), self._y1 + (self.cell_height * r)
                )
                cell = Cell(coord, self.cell_width, self.cell_height)
                cell_row.append(cell)
            self._cells.append(cell_row)
        self._draw_cells()

    def _draw_cell(self, cell):
        cell.draw(self.win, self.cell_color, self.bg_color)

    def _draw_cells(self):
        if self.win is None:
            return
        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)
                self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _build_maze(self):
        # Remove Top of Top Left cell
        self._cells[0][0].top_wall = False
        self._draw_cell(self._cells[0][0])
        self._animate()
        # Remove Bottom of Bottom Right cell
        self._cells[-1][-1].bot_wall = False
        self._draw_cell(self._cells[-1][-1])
        self._animate()
        # Recursive function to build maze
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check Bottom Cell
            if i + 1 < self.num_rows:
                if not self._cells[i + 1][j].visited:
                    to_visit.append("b")
            # Check Left Cell
            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append("l")
            # Check Right Cell
            if j + 1 < self.num_cols:
                if not self._cells[i][j + 1].visited:
                    to_visit.append("r")
            # Check Top Cell
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append("t")
            if len(to_visit) <= 0:
                self._draw_cell(self._cells[i][j])
                self._animate()
                return
            else:
                match random.choice(to_visit):
                    case "b":
                        next_i, next_j = i + 1, j
                        self._cells[i][j].bot_wall = False
                        self._cells[next_i][next_j].top_wall = False
                        self._break_walls_r(next_i, next_j)
                    case "l":
                        next_i, next_j = i, j - 1
                        self._cells[i][j].left_wall = False
                        self._cells[next_i][next_j].right_wall = False
                        self._break_walls_r(next_i, next_j)
                    case "r":
                        next_i, next_j = i, j + 1
                        self._cells[i][j].right_wall = False
                        self._cells[next_i][next_j].left_wall = False
                        self._break_walls_r(next_i, next_j)
                    case "t":
                        next_i, next_j = i - 1, j
                        self._cells[i][j].top_wall = False
                        self._cells[next_i][next_j].bot_wall = False
                        self._break_walls_r(next_i, next_j)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        # Found Goal
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        # Check Top cell
        if i > 0:
            if not current_cell.top_wall and not self._cells[i - 1][j].visited:
                current_cell.draw_move(self.win, self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    current_cell.draw_move(self.win, self._cells[i - 1][j], undo=True)
        # Check Left cell
        if j > 0:
            if not current_cell.left_wall and not self._cells[i][j - 1].visited:
                current_cell.draw_move(self.win, self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    current_cell.draw_move(self.win, self._cells[i][j - 1], undo=True)
        # Check Right cell
        if j + 1 < self.num_cols:
            if not current_cell.right_wall and not self._cells[i][j + 1].visited:
                current_cell.draw_move(self.win, self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    current_cell.draw_move(self.win, self._cells[i][j + 1], undo=True)
        # Check Bottom cell
        if i + 1 < self.num_rows:
            if not current_cell.bot_wall and not self._cells[i + 1][j].visited:
                current_cell.draw_move(self.win, self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    current_cell.draw_move(self.win, self._cells[i + 1][j], undo=True)
