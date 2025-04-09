from drawing import Cell, Line, Point
from maze import Maze
from window import Window


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)

    margin = 10
    num_rows = 12
    num_cols = 16
    cell_width = (win_width - 2 * margin) / num_cols
    cell_height = (win_height - 2 * margin) / num_rows
    maze = Maze(
        win, Point(margin, margin), num_rows, num_cols, cell_width, cell_height, seed=1
    )
    maze.solve()
    win.mainloop()


if __name__ == "__main__":
    main()
