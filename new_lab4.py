import random

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def main():
    randomize(board)

    displayBoard(board)
    tap()


def randomize(board):
    for row in board:
         for i in range(len(row)):
             box = random.randrange(0, 2, 1)
             if box == 0:
                 box = "\N{BLACK SQUARE}"
             if box == 1:
                 box = "\N{WHITE SQUARE}"
             row[i] = box
    return board


def displayBoard(board):
   for row in board:
       print(row)


def is_solved():
    pass


def tap():
    row = input("Choose a row number (0-4): ")
    col = input("Choose a column number (0-4): ")
    choice = (row, col)
    

def find_index(row, col):
    x = board[row]
    index = x[col]
    


main()
