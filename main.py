from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell_list = []
    cell_list.append(Cell(win,Point(10,10), Point(40,40)))
    cell_list.append(Cell(win,Point(10,50), Point(40,80), bottom=False,top=False))
    cell_list.append(Cell(win,Point(50,10), Point(80,40), left=False))
    cell_list.append(Cell(win,Point(90,10), Point(120,40), right=False))
    cell_list.append(Cell(win,Point(130,10), Point(160,40), top=False))
    cell_list.append(Cell(win,Point(170,10), Point(200,40), bottom=False))
    for x in cell_list:
        x.draw()    
    cell_list[0].draw_move(cell_list[1])
    cell_list[0].draw_move(cell_list[2], True)
    win.wait_for_close()

main()