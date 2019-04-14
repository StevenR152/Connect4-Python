# Connect 4 in Python   
This repository has the starting foundations of a Connect 4 game.

## What is connect four?
http://www.boardgamecapital.com/connect-four-rules.htm

## Get Started
Get started by checking out the codebase and looking over the python code.
The current codebase prints the board out each time the player makes a turn.

There are several functions already defined, but unfortunately some of the function code has gone missing!

- print_board
- get_user_input
- is_bottom_of_board
- is_board_square_empty_at_position
- place_piece
- check_win
- next_player
- play

## TODO
There is several parts of the game you can improve.

1. Make the print_board function print the board to the console.
2. Stop the user from entering bad input in the get_user_input function.
3. Make the place_peice function use the board, column and peice to place the peices in the correct grid position.
4. Complete the check_win function so the game can be won by a player and have it print the winning player.

## Write tests
Oh that sounds boring, who wants tests? Every job requires tests to make sure their software works, and continues to work. If you submit me a job application without tests, you'll fail instantly - sounds harsh right?

Look up PyTest and look at implementing tests for the following:

1. Check the player wins if 4 pieces are placed in a horizontal row
2. Check the player wins if 4 pieces are placed in a vertical row
3. Check the player wins if 4 pieces are placed in a diagonal
4. Think up other test cases for bad user input.

