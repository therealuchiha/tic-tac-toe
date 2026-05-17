import tkinter as tk
import time
from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax, minimax_alpha_beta

class TicTacToeGUI:
    def __init__(self, root):
        """Initialize the Tic Tac Toe GUI"""
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize game state
        self.board = initial_state()
        self.game_over = False
        self.ai_thinking = False
        
        # Create frame for the game board
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        
        # Create the board buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, text="", font=("Helvetica", 24), 
                                   width=5, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Create the status label
        self.status_var = tk.StringVar()
        self.status_var.set("Your turn (X)")
        self.status_label = tk.Label(root, textvariable=self.status_var, font=("Helvetica", 12))
        self.status_label.pack(pady=10)
        
        # Create the reset button
        self.reset_button = tk.Button(root, text="New Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        # Set the initial player
        self.current_player = player(self.board)
        self.update_display()
        
    def make_move(self, i, j):
        """Handle a player's move on the board"""
        if self.game_over or self.ai_thinking or self.board[i][j] is not None:
            return
        
        # Apply the human's move (X)
        action = (i, j)
        self.board = result(self.board, action)
        self.update_display()
        
        # Check for end of game
        if terminal(self.board):
            self.end_game()
            return
        
        # Trigger AI's turn
        self.ai_thinking = True
        self.status_var.set("AI is thinking...")
        self.root.update()
        
        # Add a delay to show AI is thinking
        self.root.after(100, self.ai_move)
    
    def ai_move(self):
        """Handle the AI's move"""
        ai_action = minimax(self.board)
        
        if ai_action:
            self.board = result(self.board, ai_action)
        
        self.update_display()
        self.ai_thinking = False
        
        # Check for end of game
        if terminal(self.board):
            self.end_game()
    
    def update_display(self):
        """Update the GUI display based on the current board state"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "X":
                    self.buttons[i][j].config(text="X", fg="blue")
                elif self.board[i][j] == "O":
                    self.buttons[i][j].config(text="O", fg="red")
                else:
                    self.buttons[i][j].config(text="")
        
        if not self.game_over and not self.ai_thinking:
            self.status_var.set("Your turn (X)")
    
    def end_game(self):
        """Handle logic when the game ends"""
        self.game_over = True
        game_winner = winner(self.board)
        
        if game_winner == "X":
            self.status_var.set("You win!")
        elif game_winner == "O":
            self.status_var.set("AI wins!")
        else:
            self.status_var.set("It's a tie!")
    
    def reset_game(self):
        """Reset the game to the initial state"""
        self.board = initial_state()
        self.game_over = False
        self.ai_thinking = False
        self.current_player = player(self.board)
        self.update_display()
        self.status_var.set("Your turn (X)")

if __name__ == "__main__":
    # Create the Tkinter application window and start the game
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
