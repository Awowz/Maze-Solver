from graphics import Cell, Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = int(cell_size_x)
        self._cell_size_y = int(cell_size_y)
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
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
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1,-1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            possible_direction = self.get_adjacent_not_visited(i,j)
            if len(possible_direction) == 0:
                self._draw_cell(i,j)
                return
            next_direction_x, next_direction_y = possible_direction[random.randrange(0,len(possible_direction))]
            if i == next_direction_x:
                if next_direction_y > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_direction_x][next_direction_y].has_top_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_direction_x][next_direction_y].has_bottom_wall = False
            else:
                if next_direction_x > i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_direction_x][next_direction_y].has_left_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_direction_x][next_direction_y].has_right_wall = False
            self._draw_cell(i,j)
            self._draw_cell(next_direction_x,next_direction_y)
            self._break_walls_r(next_direction_x, next_direction_y)

    def get_adjacent_not_visited(self, x, y):
        not_visited_list = []
        if x - 1 >= 0:
            if not self._cells[x - 1][y].visited:
                not_visited_list.append((x - 1, y))
        if x + 1 <= self.num_cols - 1:
            if not self._cells[x + 1][y].visited:
                not_visited_list.append((x + 1, y))
        if y - 1 >= 0:
            if not self._cells[x][y - 1].visited:
                not_visited_list.append((x, y - 1))
        if y + 1 <= self.num_rows - 1:
            if not self._cells[x][y + 1].visited:
                not_visited_list.append((x, y + 1))
        return not_visited_list
    
    def _reset_cells_visited(self):
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                self._cells[x][y].visited = False
            
    def solve(self):
        return self._solve_r(0,0)

    def _draw_navigation_line(self,x,y,next_x,next_y):
        self._cells[x][y].draw_move(self._cells[x + next_x][y + next_y])
        if self._solve_r(x + next_x,y + next_y):
            return True
        else:
            self._cells[x][y].draw_move(self._cells[x + next_x][y + next_y], True)
            return False

    def _solve_r(self, x,y):
        self._animate()
        self._cells[x][y].visited = True
        if x == self.num_cols - 1 and y == self.num_rows - 1:
            return True
        each_direction = [(0,1), (1,0),(-1,0), (0,-1)]
        for direction in each_direction:
            next_x, next_y = direction
            if ((next_x + x) >= 0 and (next_x + x) <= self.num_cols - 1) and ((next_y + y) >= 0 and (next_y + y) <= self.num_rows - 1):
                if not self._cells[x + next_x][y + next_y].visited:
                    if next_y == 0:
                        if next_x == 1:
                            if not self._cells[x][y].has_right_wall:
                                if self._draw_navigation_line(x,y,next_x,next_y):
                                    return True
                        else:
                            if not self._cells[x][y].has_left_wall:
                                if self._draw_navigation_line(x,y,next_x,next_y):
                                    return True
                    else:
                        if next_y == 1:
                            if not self._cells[x][y].has_bottom_wall:
                                if self._draw_navigation_line(x,y,next_x,next_y):
                                    return True
                        else:
                            if not self._cells[x][y].has_top_wall:
                                if self._draw_navigation_line(x,y,next_x,next_y):
                                    return True
        return False


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