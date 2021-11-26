import random

class Dice():

    def __init__(self, faceNum):
        self.faceNum = faceNum

    def roll(self,num = 1):
        result = []
        for i in range(num):
            result.append(random.randint(1,self.faceNum))
        return sum(result), result