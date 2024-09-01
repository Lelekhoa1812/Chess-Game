import tkinter as tk
from PIL import Image, ImageTk

# Game board and chess pieces
board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

class ChessBoard(tk.Canvas):
    def __init__(self, master, board):
        super().__init__(master, width=600, height=600)
        self.master = master
        self.board = board
        self.selected_piece = None

        image_path = "/Users/khoale/Downloads/Chess_Pieces/bp.png"
        self.pawn_image = ImageTk.PhotoImage(Image.open(image_path))
  
        self.pack()
        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color1 = 'brown'
                    color2 = 'sandy brown'
                else:
                    color1 = 'sandy brown'
                    color2 = 'brown'
                x1, y1 = i * 75, j * 75
                x2, y2 = (i + 1) * 75, (j + 1) * 75
                self.create_rectangle(x1, y1, x2, y2, fill=color1)
                self.create_rectangle(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill=color2)
                if self.board[i][j] != '':
                    piece = self.board[i][j]
                    x, y = x1 + 37.5, y2 - 37.5 
                    if piece.lower() == 'p':
                        self.create_image(x, y, image=self.pawn_image)
                    else:
                        if (i + j) % 2 == 0:
                            self.create_oval(x - 15, y - 15, x + 15, y + 15, fill='black' if piece.islower() else 'white')
                            self.create_text(x, y, text=piece, font=('Helvetica', 12), fill='white' if piece.islower() else 'black')
                        else:
                            self.create_oval(x - 15, y - 15, x + 15, y + 15, fill='white' if not piece.islower() else 'black')
                            self.create_text(x, y, text=piece, font=('Helvetica', 12), fill='black' if not piece.islower() else 'white')

    def on_click(self, event):
        x, y = event.x // 75, event.y // 75
        if self.board[x][y] != '':
            if self.selected_piece is None:
                self.selected_piece = (x, y)
            elif self.selected_piece == (x, y):
                self.selected_piece = None
            else:
                self.move_piece(self.selected_piece, (x, y))
                self.selected_piece = None

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece.islower():
            if start[0] < end[0]:
                piece = piece.upper()
        else:
            if start[0] > end[0]:
                piece = piece.lower()
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = ''
        self.draw_board()

root = tk.Tk()
board = ChessBoard(root, board)
root.mainloop()
