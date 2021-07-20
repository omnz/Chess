class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.board = [[0]*self.cols for _ in range(0, self.rows)]
    
    def setup(self):
        for x in range(0, self.cols):
            if(x == 0 or x == 7):
                self.board[x][0] = "R"
                self.board[x][1] = "N"
                self.board[x][2] = "B"
                self.board[x][3] = "Q"
                self.board[x][4] = "K"
                self.board[x][5] = "B"
                self.board[x][6] = "N"
                self.board[x][7] = "R"
            if(x == 1 or x == 6):
                for y in range(0, self.cols):
                    self.board[x][y] = "P"

    def display(self):
        for row in self.board:
            for x in row:
                print(f" {x} ", end='')
            print()