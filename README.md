# Maze solver

Maze solver is a simple application that generates a given number of columns and given number of rows, then a depth first search type algorithm is ran in attempt to solve the maze.

![Maze solver example](/assets/popup.gif "Maze solver example")

## Prerequisites
you will need...
* Python 3
* tkinter

## Instruction

* run the following command to generate a random 15 x 15 maze
> python3 main.py
* you can provide additional arguments that can modify the columns, rows, and the generated seed.
* Changing the number of columns can be done with -c or --colm
> python3 main.py -c 50
* Changing the number of rows can be done with -r or --row
> python3 main.py -r 50
* Changing the seed can be done with -s or --seed
> python3 main.py --seed 12345
* for more help type the argument -h or --help for the full list. 