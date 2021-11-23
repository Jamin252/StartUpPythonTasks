BOARD = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(".")
    BOARD.append(row)
NUMBERS = ["zero", "one", "two", "three", "four", "five"]
class player():
    def __init__(self, list, x):
        self.one = (x, int(list[0]))
        self.two = (x, int(list[1]))
        self.three = (x, int(list[2]))
        self.four = (x, int(list[3]))
        self.five = (x, int(list[4]))
        self.order = 1
temp1 = input("First player order: ")
temp2 = input("Second player order: ")
x = temp1.split(" ")
y = temp2.split(" ")
firstPlayer = player(x, 4)
secondPlayer = player(y, 0)
BOARD[4] = x
BOARD[0] = y
BOARD[2][2] = "*"
for i in range(1, 6):
    exec(f"BOARD[firstPlayer.{NUMBERS[i][0]}][firstPlayer.{NUMBERS[i][1]}] = 'F'")
for i in range(1, 6):
    exec(f"BOARD[secondPlayer.{NUMBERS[i][0]}][secondPlayer.{NUMBERS[i][1]}] = 'S'")

def move(y, x):
    y = int(y)
    x = int(x)
    result = []
    for i in range(1, 8):
        tempx = x
        tempy = y
        if i == 1:
            while BOARD[tempy - 1][tempx] == "." and tempy - 1 >= 0 and tempy - 1 <=4 and tempx >= 0 and tempx <= 4:
                tempy -= 1
            result.append((tempy, tempx))
        elif i == 2:
            while BOARD[tempy - 1][tempx + 1] == "." and tempy - 1 >= 0 and tempy - 1 <=4 and tempx +1 >= 0 and tempx + 1 <= 4:
                tempy -=1
                tempx +=1
            result.append((tempy, tempx))
        elif i == 3:
            while BOARD[tempy][tempx + 1] == "." and tempy >= 0 and tempy <=4 and tempx + 1 >= 0 and tempx + 1 <= 4:
                tempx +=1
            result.append((tempy, tempx))
        elif i == 4:
            while BOARD[tempy + 1][tempx + 1] == "." and tempy - 1 >= 0 and tempy - 1 <=4 and tempx >= 0 and tempx <= 4:
                tempy +=1
                tempx += 1
            result.append((tempy, tempx))
        elif i == 5:
            while BOARD[tempy + 1][tempx] == "." and tempy + 1 >= 0 and tempy + 1 <=4 and tempx >= 0 and tempx <= 4:
                tempy +=1
            result.append((tempy, tempx))
        elif i == 6:
            while BOARD[tempy + 1][tempx - 1] == "." and tempy + 1 >= 0 and tempy + 1 <=4 and tempx - 1 >= 0 and tempx - 1 <= 4:
                tempy +=1
                tempx -=1
            result.append((tempy, tempx))
        elif i == 7:
            while BOARD[tempy][tempx - 1] == "." and tempy >= 0 and tempy <=4 and tempx - 1 >= 0 and tempx - 1 <= 4:
                tempx -= 1
            result.append((tempy, tempx))
        else:
            while BOARD[tempy - 1][tempx - 1] == "." and tempy - 1 >= 0 and tempy - 1 <=4 and tempx - 1>= 0 and tempx - 1 <= 4:
                tempy -= 1
                tempx -= 1
            result.append((tempy, tempx))
    return result
counter = 1
while True:
    if counter % 2 == 1:
        temp = firstPlayer.orders
        coor =None
        print(NUMBERS[firstPlayer.order])
        exec(f"coor = firstPlayer.{NUMBERS[firstPlayer.order]}")
        results = move(coor[0], coor[1])
        print(results)
        print(BOARD)