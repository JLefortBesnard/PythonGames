# Sudoku

### First: run sudoku_generator.py:

This script builds full Sudoku grids. 
Run the script and type in:
generate_sudoku(1000). The sudoku grid is built on trial and error by the computer
thus it might require at least 500 trials to get a complete one.
The program will create a folder "sudoku" and store the full grid inside


### Second: run sudoku_game.py:
This script empties as many numbers of the sudoku as you want to make it the difficulty you want 
and then ask you to rebuild the grid. 

Run the script and type in: play()

´´´
Which level? (easy <5, medium <10, hard >15 )
´´´

The maximum of numbers to be removed. It can be a bit less than the number you chose.

The sudoku grid will then appear with missing numbers as red question mark.

´´´
To retry the same one: ctrl + c and paste:
play(path="sudoku/sudoku_temporary.xls")

which column? (btw 1 and 9)
´´´
You will first have to enter the column number, then the row number and finally the number you wanna
put in.

Once you are done, type in: play() to play again.

If you are playing with many missing values and you tried number that were actually not the good ones, you can start
again the exact same grid by typing in: ctrl + c and then typing in: play(path="sudoku/sudoku_temporary.xls").
This would restart the game with the last grid.

Have fun!

