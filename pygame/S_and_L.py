from helper import Dice
from csv import reader


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

    def __init__(self, start, end,hvImage = False, image= None):
        super().__init__(start, end)
        if hvImage:
            self.image = image
    
class Snake(Obstacal):

    def __init__(self, start, end,hvImage = False, image= None):
        super().__init__(start, end)
        if hvImage:
            self.image = image

class Game():
    def __init__(self, snakeDict, ladderDict,diceNumSides = 6, diceNum = 1,playerNum = 2):
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
        self.win = False

    def play(self):
        while True and not self.win:
            for player in self.playerGroup:
                if self.win:
                    break
                self.playerLogic(player)
                input("Press enter to go next")


    def playerLogic(self,player):
        print(f"player{player.playerNum}: position {player.position}")
        print(f"player {player.playerNum}'s Turn")
        numMove = self.dice.roll(self.diceNum)
        print(f"player rolled {numMove}")
        temp = player.position + numMove
        if temp < 100:
            player.position = temp
        elif temp == 100:
            self.win = True
            print(f"player{player.playerNum} has won")
        elif temp > 100:
            print("you have go over 100, return the original position")
        self.linkCheck(player)
        print(f"player{player.playerNum} is at {player.position}")

    def linkCheck(self, player):
        for link in self.snakeGroup:
            if player.position == link.start:
                print(f"player{player.playerNum} has got on a snake.\nplayer{player.playerNum} travelled from {player.position} to {link.end}")
                player.position = link.end
        for link in self.ladderGroup:
            if player.position == link.start:
                print(f"player{player.playerNum} has got on a ladder.\nplayer{player.playerNum} travelled from {player.position} to {link.end}")
                player.position = link.end


def main():
    ladderDict = {}
    snakeDict = {}
    with open("S_and_L.csv") as f:
        lines = reader(f)
        next(lines)
        for start, end in lines:
            start = int(start)
            end = int(end)
            if start > end:
                snakeDict[start] = end
            else:
                ladderDict[start] = end
    game = Game(snakeDict, ladderDict)
    game.play()

if __name__ == "__main__":
    main()