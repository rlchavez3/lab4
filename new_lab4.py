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
    row = int(input("Choose a row number (0-4): "))
    col = int(input("Choose a column number (0-4): "))
    choice = find_index(row, col)
    if choice == "\N{BLACK SQUARE}":
        choice = "\N{WHITE SQUARE}"
        

def change_surrounding(row, col):
    up = find_index(row + 1, col)
    down = find_index(row - 1, col)
    right = find_index(row, col + 1)
    left = find_index(row, col - 1)
    if up == "\N{BLACK SQUARE}":
        up = "\N{WHITE SQUARE}"
    else:
        up = "\N{BLACK SQUARE}"
    if down == "\N{BLACK SQUARE}":
        down = "\N{WHITE SQUARE}"
    else:
        down = "\N{BLACK SQUARE}"
    if right = "\N{BLACK SQAURE}":
        right = "\N{WHITE SQUARE}"
    else:
        right = "\N{BLACK SQUARE}"
    if left = "\N{BLACK SQUARE}":
        left = "\N{WHITE SQUARE}"
    else:
        left = "\N{BLACK SQUARE}"
    
    
    

def find_index(row, col):
    x = board[row]
    index = x[col]
    return index
    


main()
