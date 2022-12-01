import sys, os

class Player:
    def __init__(self, name, numb):
        self.playerName = name
        self.playerNumber = numb
        self.CreatePlayer()

    def CreatePlayer(self): # static method that is used to create a player instance and return it
        print("\nName: ", self.playerName, "\nToken ID: ", self.playerNumber)

    def getName(self):
        return self.playerName

    def getNumber(self):
        return self.playerNumber

    def makeMove(self, Board):
        posX = int(input("Enter which column to enter: ")) - 1
        self.columns = Board.columns

        while True:
            if posX < 0 or posX > self.columns - 1:
                posX = int(input("Invalid column. Re-enter which column to enter: ")) - 1
            elif Board.columnFull(posX) == True:
                posX = int(input("Column Full. Re-enter which column to enter: ")) - 1
            else:
                return posX

class Board:

    def __init__(self, num):
        self.columns = 0
        self.rows = 0

        self.board = []
        self.maxPlayers = num + 1
        self.CreateBoard()

        self.posY = 0

    def CreateBoard(self):
        self.columns = int(input("\nEnter the number of columns (4-10): "))
        while self.columns < 4 or self.columns > 10:
            self.columns = int(input("Invalid input. Re-enter the number of columns (4-10): "))

        self.rows = int(input("\nEnter the number of rows (4-10): "))
        while self.rows < 4 or self.rows > 10:
            self.rows = int(input("Invalid input. Re-enter the number of rows (4-10): "))

        for y in range(self.rows):
            self.board.append([])
            for x in range(self.columns):
                self.board[y].append(" ")
        print("\n BOARD CREATED")

    def display(self):
        os.system('cls')
        for i in range(1, self.columns + 1):
            print(i, end="   ")
        print("\n" + "-" * ((self.columns * 4)))
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                print(self.board[y][x], end=" | ")
            print("")
        print("-" * ((self.columns * 4)))

    def columnFull(self, posX):
        self.isColumnFull = True
        self.posY = 0
        for y in range(len(self.board) - 1, -1, -1):
            if self.board[y][posX] == " ":
                self.isColumnFull = False
                self.posY = y
                return self.isColumnFull

        return self.isColumnFull

    def boardFull(self):
        for y in range(len(self.board)):
            if " " in self.board[y]:
                return None

        print("\nDRAW")
        sys.exit()

    def getWidth(self):
        return self.columns

    def addToken(self, Numb, posX):
        self.board[self.posY][posX] = Numb

    def checkWinner(self, Players):
        winner = self.checkWinCondition()
        for player in Players:
            if player.getNumber() == winner:
                print(player.getName()+" Wins!!")
                sys.exit()

    def checkWinCondition(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                for k in range(1, self.maxPlayers):
                    count = 0
                    if self.board[y][x] == k:
                        for cond in range(0, 4):
                            count = 1
                            if cond == 0:
                                for i in range(1,4):
                                    try:
                                        if self.board[y+i][x] == k:
                                            count += 1
                                    except:
                                        pass
                                    if count == 4:
                                        return k
                            elif cond == 1:
                                for i in range(1, 4):
                                    try:
                                        if self.board[y][x+i] == k:
                                            count += 1
                                    except:
                                        pass
                                    if count == 4:
                                        return k
                            elif cond == 2:
                                for i in range(1, 4):
                                    try:
                                        if self.board[y+i][x+i] == k:
                                            count += 1
                                    except:
                                        pass
                                    if count == 4:
                                        return k
                            elif cond == 3:
                                for i in range(1, 4):
                                    try:
                                        if self.board[y+i][x-i] == k:
                                            count += 1
                                    except:
                                        pass
                                    if count == 4:
                                        return k
        return 0

    def update(self):
        self.display()
        self.boardFull()


Players = []
num = int(input("Enter the number of players: "))
while num < 2 or num > 4:
    num = int(input("Invalid input. Re-enter the number of players: "))

for x in range(1, num + 1):
    name = input("\nEnter player name: ")
    Players.append(Player(name, x))

Board = Board(num)
turn = 1
while True:
    for player in Players:
        Board.update()
        Board.checkWinner(Players)
        print(player.getName() + "'s Turn.")
        posX = player.makeMove(Board)
        Board.addToken(player.getNumber(), posX)