from helper import Dice
from csv import reader

#Obstacle Class
class Obstacle():
    """
    It will be the parent class of Snake class and Ladder class

    Innitalize:
        start
        end
    getStart:
    getEnd:
    """
    #Innitalize:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        #raise NotImplementedError

    def getStart(self):
        return self.start
        raise NotImplementedError

    def getEnd(self):
        return self.end
        raise NotImplementedError

#Snake Class
class Snake(Obstacle):
    """
    It will be child class of Obstacle. It is the snake that move player down

    Innitialize:

    """
    def __init__(self,start,end):
        super().__init__(start,end)

#Ladder Class
class Ladder(Obstacle):
    """
    It will be child class of Obstacle.
    Description: It is a ladder that move player up
    """
    def __init__(self,start,end):
        super().__init__(start,end)

#player Class
class Player():
    """
    It will be a player who the user would use 

    Innitialize: 
        Position
        Name
    
    PlayerMove(numOfMoves):
        check if the the player move to a place not over the finish lines
            if no change it to the position
    """
    #Innitialize
    def __init__(self,name):
        self.position = 0
        self.name = name
        #raise NotImplementedError

    #Playermove: It will move the player according to the move input
    def playerMove(self, numOfMoves):
        position = self.getPosition()
        target = position + numOfMoves
        return position, target
        raise NotImplementedError

    def getPosition(self):
        return self.position
        raise NotImplementedError
    
    def getName(self):
        return self.name
        raise NotImplementedError
    
    def setPosition(self, target):
        self.position = target
        return

#Game Class
class Game():
    """
    It will be a game class which the logic runs
    """

    """
    Initialize(number of player = 2, dict consist of ladders, dict consist of snakes, number of dice, number of face in a dice)

    make a dice object
    player group which consist of all the players
        Ask the player name
    input all the snake into snakeGroup
    input all laders into ladderGroup
    wincondition
    number of dice
    """
    def __init__(self,ladderDict, snakeDict, numOfPlayer = 2, numOfDice = 1, numOfFaces = 6):
        self.dice = Dice(numOfFaces)
        
        self.playerGroup = []

        #make player for numOfPlayer time
        for i in range(numOfPlayer):
            tempName = input(f"Player {i +1} Name: ")
            player = Player(tempName)
            self.playerGroup.append(player)

        self.snakeGroup = []

        #loop through snakeDict
        for key in snakeDict.keys():
            snake = Snake(key, snakeDict[key])
            self.snakeGroup.append(snake)

        self.ladderGroup = []

        #loop through ladderDict
        for key in ladderDict.keys():
            ladder = Ladder(key, ladderDict[key])
            self.ladderGroup.append(ladder)

        self.numOfDice = numOfDice
        self.winCondition = 100
            


        #raise NotImplementedError

    #play():  (The spine of the logic)
        #Loop
            #loop through each player in the player group
                #wait until user press enter to start
                #roll a dice 
                #Player move
                #check if over the end
                #check if encounter a obstacal using checkObstacal function
                #If encounter obstacal move the end of that obstacal
                #outPut to the user what have this player done
                #check if win or not using checkWin

    def play(self):
        while True:
            for player in self.playerGroup:
                input("Press Enter to continue")

                #Roll the dice
                sumOfMoves, dices = self.rollDice()

                #get the position the player will be in
                original, final = player.playerMove(sumOfMoves)

                overTheLine = False
                #check if the player will move over the end
                if self.checkEnd(final):
                    #reverse the move
                    overTheLine = True
                    final = 200 - original - sumOfMoves

                #check if the player encounter a obstacle
                start, end, moved = self.checkObstacal(final)

                #change the final to end
                final = end

                #set player to new position
                player.setPosition(final)
                
                #print output
                self.playerMovement(player,original, final,sumOfMoves,dices,moved, overTheLine,start)

                #check if win
                if self.checkWin(final):
                    self.winOutput(player)
                    exit()
                    
        #raise NotImplementedError

    #roll the dice
    def rollDice(self):
        return self.dice.roll(self.numOfDice)

    #Check if over the end
    def checkEnd(self,position):
        if position > 100:
            return True
        return False
    #print what have done in this round
    def playerMovement(self,player, original,final,sumOfMoves, dices,moved, overTheLine,start):
        print(f"player {player.getName()} rolled ", *dices,f". Total of {sumOfMoves} moves")
        print(f"player {player.getName()} has moved from {original} to {original + sumOfMoves}")

        #Check if it is over the line
        if overTheLine:
            print(f"but since it is over the line, it will go back to position {start}")

        #check if it is moved by obstacle
        if not moved == None:
            print(f"but he encounter {moved}, so he moved from {start} to {final}.")
        #raise NotImplementedError

    #checkObstacal: check if the position have a obstacle and return the start and end and 
    #bool indicate if the player has move
    def checkObstacal(self,position):
        print(f"position = {position}")
        #loop through snakes
        for snake in self.snakeGroup:

            #check is position = snake's start
            if position == snake.getStart():
                return position,snake.getEnd(), "Snake"
        
        #loop through ladders
        for ladder in self.ladderGroup:

            #check if position = ladder's start
            if position == ladder.getStart():
                return position,ladder.getEnd(), "Ladder"
        
        return position, position, None
        #raise NotImplementedError


    #checkWin: check if the player has win or not
    def checkWin(self,position):
        if position == self.winCondition:
            return True
        return False
        raise NotImplementedError

    #Output when someone win
    def winOutput(self,player):
        print(f"Player {player.getName()} has won!!")
        #raise NotImplementedError

#Main function
def main():
    #declare ladder and snake dictionary
    ladderDict = {}
    snakeDict = {}
    #open S_and_L.csv
        #reader the file
    with open("S_and_L.csv", "r") as f:
        lines = reader(f)
        next(lines)
        
        #loop through the reader objects
        for start, end in lines:
            #import into the ladder and snake dictionary
            start = int(start)
            end = int(end)
            #check if it is a ladder or snake
            if start < end:
                ladderDict[start] = end
            else:
                snakeDict[start] = end


    #ask for number of player:
    numOfPlayer = 1
    #check if number of player is valid (a positive integer larger than 1)
    while numOfPlayer < 2:
        numOfPlayer = int(input("Number of players: "))
    
    #ask for number of dice
    numOfDice = -1
    #check if number of dice is valid
    while numOfDice < 0:
        numOfDice = int(input("Number of dice: "))
    
    #ask for number of face on the dices
    numOfFaces = -1
    while numOfFaces < 3:
        numOfFaces = int(input("Number of faces on the dice: "))
    #Innitialize a game object
    game  = Game(ladderDict, snakeDict, numOfPlayer = numOfPlayer, numOfDice= numOfDice, numOfFaces= numOfFaces)
    game.play()
    #game.play
    return
    raise NotImplementedError

if __name__ == "__main__":
    main()