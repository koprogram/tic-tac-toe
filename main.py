import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

def check_draw(board):
    return " " not in board

def find_best_move(board, player):
    # Check for a winning move
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board, player):
                board[i] = " "  # Reset to empty space after check
                return i
            board[i] = " "  # Reset to empty space after check
    
    # Check for a move to block opponent's win
    opponent = "X" if player == "O" else "O"
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_winner(board, opponent):
                board[i] = " "  # Reset to empty space after check
                return i
            board[i] = " "  # Reset to empty space after check

    # Check for center
    if board[4] == " ":
        return 4
    
    # Check for corners
    corners = [0, 2, 6, 8]
    random.shuffle(corners)  # Shuffle corners to add randomness
    for i in corners:
        if board[i] == " ":
            return i
    
    # Make a random move
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves) if available_moves else None

def main():
    board = [" " for _ in range(9)]
    human_player = "X"
    ai_player = "O"
    
    current_player = human_player
    
    while True:
        print_board(board)
        if current_player == human_player:
            move = None
            while move is None:
                try:
                    move = int(input(f"Player {human_player}, choose your move (1-9): ")) - 1
                    if board[move] != " ":
                        print("That position is already taken. Choose another.")
                        move = None
                except (ValueError, IndexError):
                    print("Invalid move. Please try again.")
        else:
            print(f"AI {ai_player} is making a move...")
            move = find_best_move(board, ai_player)
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            winner = "Player" if current_player == human_player else "AI"
            print(f"{winner} {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = ai_player if current_player == human_player else human_player

if __name__ == "__main__":
    main()
