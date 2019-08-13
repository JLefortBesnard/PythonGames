import pandas as pd
import numpy as np
import glob
import os


class board:
    """
    This class create the board structure, print it, update it,
    check for winning position, highlight winning position, check if board full or still move available
    """
    def __init__(self):
        df = pd.DataFrame(0, columns = [1,2,3,4,5,6,7,8,9], index=[i+1 for i in range(9)])
        self.board = df

    def print_board(self):
        df = self.board
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

    def write_full_lign(self, list, col=None, row=None):
        if len(list) != 9:
            return "Problem len(list) != 9"
        if row != None and col != None:
            return "Problem: cannot fill col AND row at the same time"
        if col != None:
            self.board[col] = list
        elif row != None:
            self.board.loc[row] = list


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

    def save_sudoku(self, saving_number):
        df = self.board
        basedir =os.path.dirname("sudoku"")
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        existing_df_paths = glob.glob("sudoku/*")
        while os.path.exists("sudoku/sudoku_{}.xls".format(saving_number)) == True:
            saving_number += np.random.randint(10)
        df.to_excel("sudoku/sudoku_{}.xls".format(saving_number))




def create_sudoku(saving_number):
    new_sudoku = board()
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first_lign = np.random.choice(moves, size=len(moves), replace=False)
    col_ = np.random.choice(moves)
    new_sudoku.write_full_lign(first_lign, col=col_, row=None)
    for col in range(1, 10):
        for row in range(1, 10):
            # print(" ")
            # print('building column: {}, and row {}'.format(col, row))
            # print(" existing number at this position: {}".format(new_sudoku.show_case(col, row)))
            # print(" ")
            if new_sudoku.show_case(col, row) == 0:
                available_moves =  new_sudoku.return_possibility(col, row)
                if len(available_moves) != 0:
                    new_number = np.random.choice(available_moves)
                    new_sudoku.write_move(col, row, new_number)
                else:
                    # print("Failed building Sudoku")
                    return 0
    new_sudoku.save_sudoku(saving_number)
    return 1

def generate_sudoku(number_generations):
    total = 0
    for i in range(number_generations):
        sudoku = create_sudoku(i)
        total += sudoku
        print("generation {}/{}".format(i, number_generations))
        print("Successfully built = {}".format(total))
    print("Number of game successfully generated: ", total)
