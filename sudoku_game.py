import pandas as pd
import numpy as np
import glob
import os
import time
from sys import platform as sp


# clear the screen of your terminal in Linux/Mac or Windows
def clear_screen():
    if sp == "win32":
        os.system('cls')
    else:
        os.system('clear')

class board:
    """
    This class create the board structure, print it, update it,
    check for winning position, highlight winning position, check if board full or still move available
    """
    def __init__(self, path_df):
        df = pd.read_excel(path_df, index_col=0)
        self.board = df

    def empty_sudoku(self, level=5):
        df = self.board
        moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        col_to_remove = np.random.choice(moves, size=level, replace=True)
        row_to_remove = np.random.choice(moves, size=level, replace=True)
        for i in range(level):
            df[col_to_remove[i]].loc[row_to_remove[i]] = 0
        df.to_excel("sudoku/sudoku_temporary.xls")

    def print_board(self):
        df_ = self.board
        df = df_.copy()
        df = df.replace(0, '\033[91m?\033[0m')
        pos = [i+1 for i in range(9)]
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[1], df[2].loc[1],df[3].loc[1],df[4].loc[1],df[5].loc[1],df[6].loc[1],df[7].loc[1],df[8].loc[1],df[9].loc[1]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[2], df[2].loc[2],df[3].loc[2],df[4].loc[2],df[5].loc[2],df[6].loc[2],df[7].loc[2],df[8].loc[2],df[9].loc[2]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[3], df[2].loc[3],df[3].loc[3],df[4].loc[3],df[5].loc[3],df[6].loc[3],df[7].loc[3],df[8].loc[3],df[9].loc[3]))
        print('----------------------')
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[4], df[2].loc[4],df[3].loc[4],df[4].loc[4],df[5].loc[4],df[6].loc[4],df[7].loc[4],df[8].loc[4],df[9].loc[4]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[5], df[2].loc[5],df[3].loc[5],df[4].loc[5],df[5].loc[5],df[6].loc[5],df[7].loc[5],df[8].loc[5],df[9].loc[5]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[6], df[2].loc[6],df[3].loc[6],df[4].loc[6],df[5].loc[6],df[6].loc[6],df[7].loc[6],df[8].loc[6],df[9].loc[6]))
        print('----------------------')
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[7], df[2].loc[7],df[3].loc[7],df[4].loc[7],df[5].loc[7],df[6].loc[7],df[7].loc[7],df[8].loc[7],df[9].loc[7]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[8], df[2].loc[8],df[3].loc[8],df[4].loc[8],df[5].loc[8],df[6].loc[8],df[7].loc[8],df[8].loc[8],df[9].loc[8]))
        print(' {} {} {} | {} {} {} | {} {} {} '.format(df[1].loc[9], df[2].loc[9],df[3].loc[9],df[4].loc[9],df[5].loc[9],df[6].loc[9],df[7].loc[9],df[8].loc[9],df[9].loc[9]))

    def show_case(self, col, row):
        return self.board[col].loc[row]

    def write_move(self, col, row, number):
        # Write number on board
        self.board[col].loc[row] = number

    def check_possibility(self, col, row, number):
        df = self.board
        col_values = df[col].values
        row_values = df.loc[row].values
        taken_values = np.concatenate([col_values, row_values])


        square = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
        square_move = []
        square_values = []
        for key in square:
            if col in square[key]:
                square_move.append(key)
        for key in square:
            if row in square[key]:
                square_move.append(key)
        for col in square[square_move[0]]:
            for row in square[square_move[1]]:
                nb = df[col].loc[row]
                square_values.append(nb)
        taken_values = np.concatenate([taken_values, square_values])
        available_moves = np.setdiff1d(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), taken_values)

        if number in available_moves:
            return 0
        else:
            return 1

    def return_possibility(self, col, row):
        df = self.board
        col_values = df[col].values
        row_values = df.loc[row].values
        taken_values = np.concatenate([col_values, row_values])


        square = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
        square_move = []
        square_values = []
        for key in square:
            if col in square[key]:
                square_move.append(key)
        for key in square:
            if row in square[key]:
                square_move.append(key)
        for col in square[square_move[0]]:
            for row in square[square_move[1]]:
                number = df[col].loc[row]
                square_values.append(number)
        taken_values = np.concatenate([taken_values, square_values])
        available_moves = np.setdiff1d(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), taken_values)
        return available_moves

    def victory(self):
        df = self.board
        for col in df.columns:
            for row in df.index:
                if df[col].loc[row] == 0:
                    return False
        return True



def game(path_df):
    sudoku =  board(path_df)
    if path_df != "sudoku/sudoku_temporary.xls":
        level = int(input("Which level? (easy <5, medium <10, hard >15 )"))
        sudoku.empty_sudoku(level=level)
    allowed_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while sudoku.victory() == False:
        time.sleep(2)
        clear_screen()
        sudoku.print_board()
        print(" ")
        print("To retry the same sudoku grid: ctrl + c and paste:")
        print("play(path=\"sudoku/sudoku_temporary.xls\")")
        print(" ")
        col = int(input("which column? (btw 1 and 9)"))
        while col not in allowed_moves:
            print("choices must be btw 1 and 9")
            col = int(input("which column? (btw 1 and 9)"))
        print(" ")
        row = int(input("which row? (btw 1 and 9)"))
        while row not in allowed_moves:
            print("choices must be btw 1 and 9")
            row = int(input("which column? (btw 1 and 9)"))
        print(" ")
        number = int(input("which number? (btw 1 and 9)"))
        while number not in allowed_moves:
            print("choices must be btw 1 and 9")
            number = int(input("which column? (btw 1 and 9)"))
        print(" ")
        if sudoku.show_case(col, row) == 0:
            if sudoku.check_possibility(col, row, number) == 0:
                sudoku.write_move(col, row, number)
            else:
                print("Forbiden move")
        else:
            print("Case already full")
    print("VICTORY!!!!")

def play(path=0):
    list_games_path = glob.glob('sudoku/*')
    index = np.random.randint(len(list_games_path))
    if path == 0:
        game(list_games_path[index])
    else:
        game(path)
