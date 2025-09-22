import random

# Function to print the game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the game is a tie
def check_tie(board):
    for row in board:
        if " " in row:  # still empty space
            return False
    return True

# Function for AI to make a move (random empty spot)
def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

# Main game loop
def play_game():
    # Initialize board
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    print("Choose row and column number between 1–3")
    print_board(board)

    while True:
        # Player move
        try:
            row = int(input("Enter row (1-3): ")) - 1  # subtract 1 to match Python index
            col = int(input("Enter col (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers between 1 and 3.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = "X"  # Player is X
        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        # AI move
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = "O"  # AI is O
        print(f"Computer placed O at row {ai_row+1}, column {ai_col+1}")
        print_board(board)

        if check_win(board, "O"):
            print("Computer wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

# Run the game
play_game()
