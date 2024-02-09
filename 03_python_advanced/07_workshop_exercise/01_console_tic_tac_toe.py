import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.BOARD_SIZE = 3
        self.board = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.current_player = 1
        self.create_board()

    def create_board(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                button = tk.Button(
                    self.window, text="",
                    font=("Arial", 50),
                    height=2,
                    width=6,
                    bg="grey",
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                button.grid(row=i, column=j, sticky="nsew")

    def handle_click(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = "X" if self.current_player == 1 else "O"
            self.current_player = 2 if self.current_player == 1 else 1

            button = self.window.grid_slaves(row=row, column=col)[0]
            button.config(text=self.board[row][col])

            self.check_for_winner()

    def check_for_winner(self):
        winner = None

        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]
                break

        for col in range(len(self.board)):
            if all(self.board[row][col] == self.board[0][col] for row in range(self.BOARD_SIZE)) \
                    and self.board[0][col] != 0:
                winner = self.board[0][col]
                break

        if all(self.board[i][i] == self.board[0][0] for i in range(self.BOARD_SIZE)) and self.board[0][0] != 0:
            winner = self.board[0][0]
        elif all(self.board[i][self.BOARD_SIZE - 1 - i] == self.board[0][self.BOARD_SIZE - 1]
                 for i in range(self.BOARD_SIZE)) and self.board[0][self.BOARD_SIZE - 1] != 0:
            winner = self.board[0][self.BOARD_SIZE - 1]

        if all(all(cell != 0 for cell in row) for row in self.board) and winner is None:
            winner = "tie"

        if winner:
            self.declare_winner(winner)

    def declare_winner(self, winner):
        message = "It's a tie!" if winner == "tie" else f"Player {winner} wins!"
        answer = messagebox.askyesno("Game Over", f"{message} Do you want to restart the game?")

        if answer:
            self.reset_game()
        else:
            self.window.quit()

    def reset_game(self):
        self.board = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]

        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.config(text="")

        self.current_player = 1

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
