from graphics import Window, Line, Point, Cell
from maze import Maze
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--colm", type=int,help="Change the number of colms generated.")
    parser.add_argument("-r", "--row", type=int,help="Change the number of rows generated.")
    parser.add_argument("-s", "--seed", type=int,help="Set a seed for maze generation.")
    args = parser.parse_args()

    num_rows = 15
    num_colms = 15
    margin = 10
    screenx = 800
    screeny = 600
    seed = None

    if args.colm:
        num_colms = abs(args.colm)

    if args.row:
        num_rows = abs(args.row)

    if args.seed:
        seed = abs(args.seed)    

    cell_size_x = (screenx - 2 * margin) / num_colms
    cell_size_y = (screeny - 2 * margin) / num_rows
    win = Window(screenx, screeny)

    maze = Maze(margin, margin,num_rows, num_colms, cell_size_x, cell_size_y, win, seed)

    if maze.solve():
        print("MAZE SOLVED!")
    else:
        print("Maze couldnt be solved")

    win.wait_for_close()

main()