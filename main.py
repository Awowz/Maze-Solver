from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    temp_line = Line(Point(50,35), Point(300,300))
    win.draw_line(temp_line, "red")
    win.wait_for_close()

main()