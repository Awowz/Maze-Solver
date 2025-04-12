from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(master=self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_window_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running:
            self.redraw()
        print("Window has been closed.\nExiting...")
    
    def close(self):
        self.__is_window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.pos1.x, self.pos1.y, self.pos2.x, self.pos2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window, top_left_pos, bottom_right_pos, left=True,right=True,top=True,bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._top_left_pos = top_left_pos
        self._bottom_right_pos = bottom_right_pos
        self._win = window
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        top_c = bottom_c = right_c = left_c = "white"
        if self.has_top_wall: top_c = "black"
        if self.has_bottom_wall: bottom_c = "black"
        if self.has_right_wall: right_c = "black"
        if self.has_left_wall: left_c = "black"
        
        top = Line(Point(self._top_left_pos.x, self._top_left_pos.y), Point(self._bottom_right_pos.x, self._top_left_pos.y))
        self._win.draw_line(top, top_c)
        
        bottom = Line(Point(self._top_left_pos.x, self._bottom_right_pos.y), Point(self._bottom_right_pos.x, self._bottom_right_pos.y))
        self._win.draw_line(bottom, bottom_c)
        
        right = Line(Point(self._bottom_right_pos.x, self._top_left_pos.y), Point(self._bottom_right_pos.x, self._bottom_right_pos.y))
        self._win.draw_line(right, right_c)
        
        left = Line(Point(self._top_left_pos.x, self._top_left_pos.y), Point(self._top_left_pos.x, self._bottom_right_pos.y))
        self._win.draw_line(left, left_c)
        
    def get_center(self) -> Point:
        distance_x = abs(self._bottom_right_pos.x - self._top_left_pos.x) // 2
        distance_y = abs(self._bottom_right_pos.y - self._top_left_pos.y) // 2
        return Point(self._top_left_pos.x + distance_x, self._top_left_pos.y + distance_y)
        
    def draw_move(self, to_cell, undo=False):
        line_color = "green"
        if undo:
            line_color = "red"
        line_connection = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line_connection, line_color)