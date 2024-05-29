class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 17)

    def is_winner(self, player):
        for i in range(9):
            for j in range(5):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] == self.board[i][j + 4] == player:
                    return True
                if self.board[j][i] == self.board[j + 1][i] == self.board[j + 2][i] == self.board[j + 3][i] == self.board[j + 4][i] == player:
                    return True
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == self.board[i + 4][j + 4] == player:
                    return True
                if self.board[i][8 - j] == self.board[i + 1][7 - j] == self.board[i + 2][6 - j] == self.board[i + 3][5 - j] == self.board[i + 4][4 - j] == player:
                    return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.print_board()
            row = int(input("Nhập hàng: "))
            col = int(input("Nhập cột: "))

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player

                if self.is_winner(self.current_player):
                    print(f"Người chơi {self.current_player} chiến thắng!")
                    break
                elif self.is_board_full():
                    print("Trận đấu hòa!")
                    break
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Ô đã được chọn. Chọn ô khác.")

game = TicTacToe()
game.play()