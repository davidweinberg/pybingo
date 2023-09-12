# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_BingoCard.ipynb.

# %% auto 0
__all__ = ['BingoCard']

# %% ../nbs/01_BingoCard.ipynb 3
class BingoCard:
    "A class representing a numeric-only version of a Bingo Card"
    def __init__(self, 
                 data,  # 2D array of integers representing the Bingo card
                 diagonal_wins:bool=False # if diagonal wins are allowed
                ):
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.picked = []

        self.loadCard(data)
        self.won = False
        self.diagonal_wins = diagonal_wins


    def loadCard(self,data):
        "Loads the data provided into the Bingo card"
        for i in range(5):
            for j in range(5):
                choice = int(data[i][j])
                self.playBoard[i][j] = choice
                self.position[choice] = (i,j)

    def updateCard(self,
                   val:int
                  ):    
        "Searches for the value provided, if found, will mark it with an X."
        try:
            x,y = self.position[val]
            self.playBoard[x][y] = 'X'
            self.updateBingo(x,y)
            self.picked.append(val)
            #if self.checkBingo(): self.won = True
        except KeyError:
            return

    def isSelected(self, x:int, y:int):
        "Check if a location has an 'X'"
        return self.playBoard[x][y] == 'X'

    def isWinner(self):
        "Checks if the card has won Bingo"
        return (self.checkBingo())

    def updateBingo(self, 
                    x:int, # x position 
                    y:int  # y position
                   ):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y:
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1

    def checkBingo(self):
        if (self.diagonal_wins):
            return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]
        else:
            return 5 in self.bingo["row"] or 5 in self.bingo["col"]
            
    def sumBoard(self):
        total = 0
        for i in range(5):
            for j in self.playBoard[i]:
                if j!='X':                   
                    total += int(j)
        return total

    def displayCard():
        print(self)
        
    def __str__(self):
        result = ""
        for i in range(5):
            for j in self.playBoard[i]:
                if j=='X':
                   result += f" {j}"
                elif j>9:
                    result += f"{j}"
                else:
                    result += f"0{j}"
                    
                result += " "
            result += "\n"
        return (result)

    __repr__ = __str__
