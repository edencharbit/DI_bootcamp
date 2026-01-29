# Mini-Project - Tic Tac Toe


def display_board(board):
    """Step 2: Displaying the Game Board"""
    for i in range(3):
        print(f" {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}")
        if i < 2:
            print("--- | --- | ---")


def helper_player_input(row, column):
    """Step 3 Helper: check if the row and col are valid"""
    flag_dim = 1
    flag_empty = 1
    if 1 <= row <= 3 and 1 <= column <= 3 and board[row - 1][
        column - 1] != " ":
        flag_empty = 0
    if row < 1 or row > 3 or column < 1 or column > 3:
        flag_dim = 0
    return [flag_empty * flag_dim, flag_dim, flag_empty]


def player_input(player):
    """Step 3: Getting Player Input"""
    print(f"Player {player}'s turn ...")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    while helper_player_input(row, column)[0] == 0:
        if helper_player_input(row, column)[1] == 0:
            print("Your move is not valid, please enter row and column in "
                  "the right dimensions")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
        elif helper_player_input(row, column)[2] == 0:
            print("Your move is not valid, please choose an empty cell")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
    for i in range(3):
        if i == row - 1:
            for j in range(3):
                if j == column - 1:
                    board[i][j] = player
    display_board(board)


def check_win(board, player):
    """Step 4: Checking for a Winner"""
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    else:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
            elif board[i][0] == board[i][1] == board[i][2] == player:
                return True
    return False


def helper_check_tie(board):
    """Step 5 Helper: Check if the board is full"""
    is_full = True
    for row in board:
        for cell in row:
            if cell == ' ':
                is_full = False
                break
        if not is_full:
            break
    return is_full


def check_tie(board):
    """Step 5: Checking for a Tie"""
    if helper_check_tie(board) and check_win(board,
                                             'X') == False and check_win(board,
                                                                         'O') == False:
        return True
    return False


def switch_player(current_player):
    """Step 6 Helper: switch the players"""
    next_player = 'X'
    if current_player == 'X':
        next_player = 'O'
    return next_player


def play():
    """Step 6: The Main Game Loop"""
    display_board(board)
    current_player = 'X'
    while check_win(board, 'X') == False or check_win(board,
                                                      'O') == False or check_tie(
            board) == False:
        player_input(current_player)
        if check_win(board, current_player) or check_tie(board):
            break
        else:
            current_player = switch_player(current_player)
    if check_win(board, current_player):
        print(f'The winner is the player {current_player}')
    elif check_tie(board):
        print('There is no winner, there is a tie')


"""Step 1: Representing the Game Board"""
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

play()
