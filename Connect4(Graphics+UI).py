
import sys
import turtle

class Player:
    def __init__(self, name, numb):
        self.playerName = name
        self.playerNumber = numb
        self.CreatePlayer()
        
    def CreatePlayer(self):
        print("\nName: ", self.playerName, "\nToken ID: ",self.playerNumber)

    def getName(self):
        return self.playerName

    def getNumber(self):
        return self.playerNumber
    
    def makeMove(self, columns):
        posX = int(turtle.textinput("Place token", "Enter which column to enter: ")) - 1
        self.columns = columns

        while True:
            if posX < 0 or posX > self.columns - 1:
                posX = int(turtle.textinput("Place token","Invalid column. Re-enter which column to enter: ")) - 1
            elif Board.columnFull(posX) == True:
                posX = int(turtle.textinput("Place token","Column Full. Re-enter which column to enter: ")) - 1
            else:
                return posX
        

class Board:
    def __init__(self, num):
        self.columns = 0
        self.rows = 0
        self.board = self.CreateBoard()
        
        self.screenWidth = self.columns*60
        self.screenHight = self.rows*60
        self.wn = self.setupScreen()

        self.maxPlayers = num+1
        self.posY = 0

    def setupScreen(self):
        wn = turtle.Screen()
        wn.title("Connect 4")
        wn.bgcolor("black")
        wn.setup(self.screenWidth+50, self.screenHight+50)
        wn.tracer(0)

        return wn

    def CreateBoard(self):
        self.columns = int(turtle.textinput("Board dimensions","\nEnter the number of columns: "))
        while self.columns < 4 or self.columns > 10:
            self.columns = int(turtle.textinput("Board dimensions","Invalid input. Re-enter the number of columns: "))

        self.rows = int(turtle.textinput("Board dimensions","\nEnter the number of rows: "))
        while self.rows < 4 or self.rows > 10:
            self.rows = int(turtle.textinput("Board dimensions","Invalid input. Re-enter the number of rows: "))

        board = []
        for y in range(self.rows):
            board.append([])
            for x in range(self.columns):
                board[y].append(" ")
        print("\n BOARD CREATED")
        return board

    def display(self):
        turtle.addshape(name=r"Connect4\assests\RedToken.gif", shape=None)
        turtle.addshape(name=r"Connect4\assests\YellowToken.gif", shape=None)
        turtle.addshape(name=r"Connect4\assests\WhiteToken.gif", shape=None)
        turtle.addshape(name=r"Connect4\assests\BlackToken.gif", shape=None)
        turtle.addshape(name=r"Connect4\assests\BgCell.gif", shape=None)

        RedToken = turtle.Turtle()
        RedToken.color("white")
        RedToken.shape(r"Connect4\assests\RedToken.gif")
        RedToken.speed(0)
        RedToken.penup()
        RedToken.hideturtle()

        YellowToken = turtle.Turtle()
        YellowToken.color("white")
        YellowToken.shape(r"Connect4\assests\YellowToken.gif")
        YellowToken.speed(0)
        YellowToken.penup()
        YellowToken.hideturtle()

        WhiteToken = turtle.Turtle()
        WhiteToken.color("white")
        WhiteToken.shape(r"Connect4\assests\WhiteToken.gif")
        WhiteToken.speed(0)
        WhiteToken.penup()
        WhiteToken.hideturtle()

        BlackToken = turtle.Turtle()
        BlackToken.color("white")
        BlackToken.shape(r"Connect4\assests\BlackToken.gif")
        BlackToken.speed(0)
        BlackToken.penup()
        BlackToken.hideturtle()

        Bgcell = turtle.Turtle()
        Bgcell.color("white")
        Bgcell.shape(r"Connect4\assests\BgCell.gif")
        Bgcell.speed(0)
        Bgcell.penup()
        Bgcell.hideturtle()

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                posX = -(self.screenWidth/2) + (x*60) + 30
                posY = (self.screenHight/2) - (y*60) - 30

                Bgcell.goto(posX, posY)
                Bgcell.stamp()
                if self.board[y][x] == 1:
                    YellowToken.goto(posX, posY)
                    YellowToken.stamp()
                elif self.board[y][x] == 2:
                    RedToken.goto(posX, posY)
                    RedToken.stamp()
                elif self.board[y][x] == 3:
                    WhiteToken.goto(posX, posY)
                    WhiteToken.stamp()
                elif self.board[y][x] == 4:
                    BlackToken.goto(posX, posY)
                    BlackToken.stamp()
                    
    def columnFull(self, posX):
        isColumnFull = True
        self.posY = 0
        for y in range(len(self.board) - 1, -1, -1):
            if self.board[y][posX] == " ":
                isColumnFull = False
                self.posY = y
                return isColumnFull

        return isColumnFull

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
        self.wn.update()
        self.display()
        self.boardFull()           

Players = []
num = int(input("Enter the number of players: "))
while num < 2 or num > 4:
    num = int(input("Invalid input. Re-enter the number of players: "))
    
for x in range(1,num+1):
    name = input("\nEnter player name: ")
    Players.append(Player(name, x))

Board = Board(num)
while True:
    for player in Players:
        Board.update()
        Board.checkWinner(Players) 
        posX = player.makeMove(Board.columns)
        Board.addToken(player.getNumber(), posX)