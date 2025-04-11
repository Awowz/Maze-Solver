from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    num_rows = 15
    num_colms = 15
    margin = 10
    screenx = 800
    screeny = 600
    cell_size_x = (screenx - 2 * margin) / num_colms
    cell_size_y = (screeny - 2 * margin) / num_rows
    win = Window(screenx, screeny)

    maze = Maze(margin, margin,num_rows, num_colms, cell_size_x, cell_size_y, win)

    win.wait_for_close()

main()