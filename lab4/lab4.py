# tic_tac_toe.py
import random


# ========== Player Base Class ==========
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        """Abstract method - will be implemented by subclasses"""
        raise NotImplementedError("Subclass must implement this method")


# ========== Human Player ==========
class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                pos = int(input(f"{self.name} ({self.symbol}), choose a position (1-9): "))
                if pos < 1 or pos > 9:
                    print("❌ Invalid choice. Choose between 1 and 9.")
                    continue
                if not board.update(pos, self.symbol):
                    print("❌ This position is already taken. Try again.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a number between 1 and 9.")


# ========== Computer Player ==========
class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        available_moves = board.get_available_positions()
        pos = random.choice(available_moves)  # Simple random strategy
        board.update(pos, self.symbol)


# ========== Board ==========
class Board:
    def __init__(self):
        # Encapsulation: keep grid private
        self.__grid = [" " for _ in range(9)]

    def display(self):
        print("\n")
        print(f" {self.__grid[0]} | {self.__grid[1]} | {self.__grid[2]} ")
        print("---|---|---")
        print(f" {self.__grid[3]} | {self.__grid[4]} | {self.__grid[5]} ")
        print("---|---|---")
        print(f" {self.__grid[6]} | {self.__grid[7]} | {self.__grid[8]} ")
        print("\n")

    def update(self, position, symbol):
        index = position - 1
        if self.__grid[index] == " ":
            self.__grid[index] = symbol
            return True
        return False

    def get_available_positions(self):
        return [i + 1 for i, val in enumerate(self.__grid) if val == " "]

    def check_winner(self):
        # Winning combinations (rows, columns, diagonals)
        winning_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in winning_combos:
            if self.__grid[a] == self.__grid[b] == self.__grid[c] != " ":
                return self.__grid[a]  # return the winner symbol
        return None

    def is_full(self):
        return " " not in self.__grid

    def __str__(self):
        # Special method for print(board)
        return f"{self.__grid[0:3]}\n{self.__grid[3:6]}\n{self.__grid[6:9]}"


# ========== Game ==========
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # index of current player

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        print("\n🎮 Game Start! 🎮\n")
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            self.board.display()

            winner_symbol = self.board.check_winner()
            if winner_symbol:
                print(f"🏆 {current_player.name} wins with '{winner_symbol}'! 🏆")
                break
            if self.board.is_full():
                print("🤝 It's a draw!")
                break

            self.switch_turns()


# ========== Main ==========
def main():
    print("Welcome to Tic-Tac-Toe!")
    choice = input("Do you want to play with a friend (1) or vs computer (2)? ")

    if choice == "1":
        name1 = input("Enter name for Player 1: ")
        name2 = input("Enter name for Player 2: ")
        player1 = HumanPlayer(name1, "X")
        player2 = HumanPlayer(name2, "O")

    elif choice == "2":
        name1 = input("Enter your name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = ComputerPlayer("Computer", "O")

    else:
        print("Invalid choice! Exiting...")
        return

    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
