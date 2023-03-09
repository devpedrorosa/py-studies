import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title('Jogo da Velha')
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 50), width=2, height=1, command=lambda x=i, y=j: self.play(x, y))
                self.buttons[i][j].grid(row=i, column=j)
        tk.mainloop()

    def play(self, i, j):
        if self.board[i][j] == '':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_win():
                tk.messagebox.showinfo('Fim do jogo', f'Jogador {self.current_player} ganhou!')
                self.root.quit()
            elif self.check_tie():
                tk.messagebox.showinfo('Fim do jogo', 'Empate!')
                self.root.quit()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True

if __name__ == '__main__':
    game = TicTacToe()