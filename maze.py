from graphics import Cell, Point
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = int(cell_size_x)
        self._cell_size_y = int(cell_size_y)
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        print(f"steps: {self._cell_size_x}  starting range: {self._x1}  end range: {self._x1 + (self.num_cols * self._cell_size_x)}")
        for colm_x in range(self._x1, self._x1 + (self.num_cols * self._cell_size_x), self._cell_size_x):
            colum_cells = []
            for row_y in range(self._y1, self._y1 + (self.num_rows * self. _cell_size_y), self._cell_size_y):
                top_left = Point(colm_x, row_y)
                bottom_right = Point(colm_x + self._cell_size_x, row_y + self._cell_size_y)
                colum_cells.append(Cell(self._win, top_left, bottom_right))
            self._cells.append(colum_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        print("meow")
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1,-1)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)