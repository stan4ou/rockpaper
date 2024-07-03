# main.py

import random

# Function to print colored text
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

# Function to get computer's move
def get_computer_move():
    moves = ['r', 'p', 's']
    return random.choice(moves)

# Function to determine the winner
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Draw"
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        return "Player wins"
    else:
        return "Computer wins"

# Function to map move to its name
def move_to_name(move):
    if move == 'r':
        return 'Rock'
    elif move == 'p':
        return 'Paper'
    elif move == 's':
        return 'Scissors'

# Function to play the game
def play_game():
    player_score = 0
    computer_score = 0
    while True:
        prCyan("Enter your move (r for rock, p for paper, s for scissors): ")
        player_move = input().lower()
        if player_move not in ['r', 'p', 's']:
            prRed("Invalid move. Exiting the game.")
            break

        computer_move = get_computer_move()
        prYellow(f"Computer chose {move_to_name(computer_move)}")

        result = determine_winner(player_move, computer_move)
        if result == "Player wins":
            player_score += 1
            prGreen("You win this round!")
        elif result == "Computer wins":
            computer_score += 1
            prRed("Computer wins this round!")
        else:
            prYellow("This round is a draw.")

        prCyan(f"Score: Player {player_score} - {computer_score} Computer")

        prCyan("Do you want to play again? (y/n): ")
        play_again = input().lower()
        if play_again != 'y':
            break

# Run the game
if __name__ == "__main__":
    play_game()
