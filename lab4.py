import random
white = "\N{WHITE SQUARE}"
black = "\N{BLACK SQUARE}"
board = [
    [white, white, white, white, white],
    [white, white, white, white, white],
    [white, white, white, white, white],
    [white, white, white, white, white],
    [white, white, white, white, white]
]


def main():
    randomize(board)
    moves = 0
    while is_solved(board) == False:
        display_board(board)
        (row, col) = get_row_col()
        tap(board, row, col)
        moves += 1
    display_board(board)
    print(f"You won with {moves} moves!")


def randomize(board):
    for i in range(random.randint(0, 20)):
        tap(board, random.randint(0, 4), random.randint(0, 4))
    return board
     


def display_board(board):
    for row in board:
        print(row)


def is_solved(board):
    check = 0
    for row in range(0, 5):
        for col in range(0, 5):
            if board[row][col] == black:
                check += 1
    if check == 25:
        return True
    else:
        return False


def get_row_col():
    row = int(input("Choose a row number (0-4): "))
    col = int(input("Choose a column number (0-4): "))
    return (row, col)


def tap(board, row, col):
    choice = board[row][col]
    if choice == white:
        board[row][col] = black
    else:
        board[row][col] = white
    change_surrounding(board, row, col)
    return board


def change_surrounding(board, row, col):
    choice = where(row, col)
    if choice == 'middle':
        if board[row - 1][col] == white:
            board[row - 1][col] = black
        else:
            board[row - 1][col] = white
        if board[row + 1][col] == white:
             board[row + 1][col] = black
        else:
            board[row + 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'top':
        if board[row + 1][col] == white:
            board[row + 1][col] = black
        else:
            board[row + 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'bottom':
        if  board[row - 1][col]  == white:
             board[row - 1][col] = black
        else:
            board[row - 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'topboard[row][col - 1]':
        if board[row + 1][col] == white:
            board[row + 1][col] = black
        else:
            board[row + 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
    elif choice == 'topboard[row][col + 1]':
        if board[row + 1][col] == white:
            board[row + 1][col] = black
        else:
           board[row + 1][col] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'bottomboard[row][col - 1]':
        if  board[row - 1][col]  == white:
             board[row - 1][col] = black
        else:
             board[row - 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
    elif choice == 'bottomboard[row][col + 1]':
        if  board[row - 1][col]  == white:
             board[row - 1][col] = black
        else:
             board[row - 1][col] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'board[row][col + 1]':
        if board[row - 1][col] == white:
            board[row - 1][col] = black
        else:
            board[row - 1][col] = white
        if board[row + 1][col] == white:
            board[row + 1][col] = black
        else:
            board[row + 1][col] = white
        if board[row][col - 1] == white:
            board[row][col - 1] = black
        else:
            board[row][col - 1] = white
    elif choice == 'board[row][col - 1]':
        if board[row - 1][col] == white:
            board[row - 1][col] = black
        else:
            board[row - 1][col] = white
        if board[row + 1][col] == white:
            board[row + 1][col] = black
        else:
            board[row + 1][col] = white
        if board[row][col + 1] == white:
            board[row][col + 1] = black
        else:
            board[row][col + 1] = white
    return board


def where(row, col):
    #determining if choice is an edge or corner
    choice = ''
    if row == 0:
        choice += 'top'
    elif row == 4:
        choice += 'bottom'
    if col == 0:
        choice += 'board[row][col - 1]'
    elif col == 4:
        choice += 'board[row][col + 1]'
    if choice == '':
        choice += 'middle'
    return choice


def tests():
    print(where(0, 4))
    print(where(3, 2))
    print(where(0, 0))
    print(where(3, 4))
    print(where(0, 2))
    print(where(4, 0))

main()
