def print_board(board):
    print("Printing the board...")
    # write code that prints the board 2d array


def get_user_input(valid_inputs, player):
    users_input = input("Enter the move for player " + str(player) + ":")
    print("User entered: " + users_input)
    # TODO Use valid_inputs to check the users input and ask them for a new input if its wrong.
    return int(users_input)


def is_bottom_of_board(board, row_index):
    return row_index == len(board) - 1


def is_board_square_empty_at_position(board, row_index, col_index):
    return board[row_index][col_index] != 0


def place_piece(board, col, piece):
    print("Place piece: " + str(col))
    row_index = 0
    piece_placed = False

    while row_index < len(board) and not piece_placed:
        # This function needs to have the board coordinates
        # calculated correctly replace the zero's with actual positions.
        if is_board_square_empty_at_position(board, row_index, col):
            board[0][0] = piece
            piece_placed = True
        elif is_bottom_of_board(board, row_index):
            board[0][0] = piece
            piece_placed = True

        row_index += 1


def check_win(board):
    # TODO Work out if the game is over
    # The objective of the game is to be the first to form a horizontal,
    # vertical, or diagonal line of four of one's own pieces.
    # TODO Print the player who won and return True to end the game.
    return False


def next_player(player):
    if player == 1:
        return 2
    if player == 2:
        return 1


def play(board):
    is_game_over = False
    player = 1
    # TODO currently the game supports any input, make the users input restricted to the following.
    valid_inputs = [1, 2, 3, 4, 5, 6, 7]

    while not is_game_over:
        print_board(board)
        col = get_user_input(valid_inputs, player)
        place_piece(board, col, player)
        is_game_over = check_win(board)
        player = next_player(player)


game_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

play(game_board)
