from helper import Dice


WIN_CONDITION = 100

class Player():
    
    def __init__(self, playerNum):
        self.playerNum = playerNum
        self.position = 0

class Obstacal():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def check(self,coor):
        if coor == self.start:
            return self.end
        return None

class Ladder(Obstacal):

    def __init__(self, hvImage = False, image= None):
        if hvImage:
            self.image = image
    
class Snake(Obstacal):

    def __init__(self, hvImage = False, image= None):
        if hvImage:
            self.image = image

class Game():
    def __init__(self, snakeDict, ladderDict,diceNumSides, diceNum,playerNum = 2):
        self.playerGroup = [] 
        for i in range(playerNum):
            self.playerGroup.append(Player(i+1))
        self.snakeGroup = []
        self.ladderGroup = []
        self.obstacalGroup = set()
        for key in snakeDict.keys():
            snake = Snake(key, snakeDict[key])
            self.snakeGroup.append(snake)
            self.obstacalGroup.add(snake)
        for key in ladderDict.keys():
            ladder = Ladder(key, ladderDict[key])
            self.ladderGroup.append(ladder)
            self.obstacalGroup.add(ladder)
        self.winCondition = WIN_CONDITION
        self.diceNum = diceNum
        self.dice = Dice(diceNumSides)
        

        
