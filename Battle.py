import os
import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def hit(self):
        self.hits += 1
        return self.hits == self.size

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(7)] for _ in range(7)]
        self.ships = [Ship(3), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]
        self.shots = set()

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
    print("  A B C D E F G")
    for i in range(7):
        print(f"{i + 1}|{' '.join(board[i])}|")

def place_ships_randomly(player):
    for ship in player.ships:
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(1, 7)
                col = random.randint(1, 7 - ship.size + 1)
            else:
                row = random.randint(1, 7 - ship.size + 1)
                col = random.randint(1, 7)

            # Check if the chosen cells are empty
            if all(player.board[row - 1][c - 1] == ' ' for c in range(col, col + ship.size)):
                for c in range(col, col + ship.size):
                    player.board[row - 1][c - 1] = 'S'
                break

def take_shot(player):
    while True:
        try:
            shot_input = input("Enter your shot (e.g., A5): ").upper()
            col = ord(shot_input[0]) - ord('A') + 1
            row = int(shot_input[1])
            if 1 <= row <= 7 and 1 <= col <= 7 and (row, col) not in player.shots:
                player.shots.add((row, col))
                return row, col
            else:
                print("Invalid shot. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid shot.")

def check_victory(player):
    return all(ship.hits == ship.size for ship in player.ships)

def main():
    print("Welcome to Battleship!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    place_ships_randomly(player)

    while not check_victory(player):
        display_board(player.board)
        row, col = take_shot(player)
        # Implement the logic to handle the shot and update the board here

    print(f"Congratulations, {player.name}! You won in {len(player.shots)} shots.")

if __name__ == "__main__":
    main()
