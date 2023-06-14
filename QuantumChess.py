class QuantumChess:
    def __init__(self):
        self.board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                      ["P", "P", "P", "P", "P", "P", "P", "P"],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      ["p", "p", "p", "p", "p", "p", "p", "p"],
                      ["r", "n", "b", "q", "k", "b", "n", "r"]]

    def move(self, from_square, to_square):
        from_x, from_y = from_square
        to_x, to_y = to_square

        piece = self.board[from_x][from_y]
        self.board[to_x][to_y] = piece
        self.board[from_x][from_y] = " "

    def display(self):
        print("   a b c d e f g h")
        for i in range(8):
            print(8 - i, " ", end="")
            for j in range(8):
                print(self.board[i][j], end=" ")
            print(8 - i)
        print("   a b c d e f g h")

def main():
    chess = QuantumChess()

    # Make a move
    chess.move((6, 3), (4, 3))

    # Display the chessboard
    chess.display()

if __name__ == "__main__":
    main()
