import copy, time

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def numberdifference(numfrom, numto):
    numberfrom = copy.deepcopy(numfrom)
    numberto = copy.deepcopy(numto)
    tempto = copy.deepcopy(numberto)
    tempfrom = copy.deepcopy(numberfrom)
    for i in tempto:
        for k in tempfrom:
            if i == k:
                numberto.remove(i)
                numberfrom.remove(k)
                tempfrom.remove(k)
                break
    return len(numberto) + len(numberfrom)

class Node():
    def __init__(self, value):
        self.action_made = 0
        result = []
        for k in str(value):
            for n in NUMBERS[int(k)]:
                result.append(n)
        self.value = result
        self.number = value

    def neighbour(self):
        result = []
        for i in range(1000):
            if i == self.number:
                continue
            numberto = []
            for k in str(i):
                for n in NUMBERS[int(k)]:
                    numberto.append(n)
            if numberdifference(self.value, numberto) <= 5:
                result.append(i)
        return result

class Frontier():
    def __init__(self):
        self.frontier = []
        self.priority = []

    def remove(self):
        if len(self.priority) != 0:
            node = self.priority[0]
            self.priority = self.priority[1:]
            return node
        elif len(self.frontier) != 0:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        else:
            return None

    def contain(self, number):
        for node in self.frontier:
            if node.number == number:
                return True
        return False

def main(temp):
    print(temp)
    temp1 = temp.split(" ")
    number = int(temp1[0])
    number_value = []
    for k in str(number):
        for i in NUMBERS[int(k)]:
            number_value.append(i)
    target = int(temp1[1])
    target_value = []
    for k in str(target):
        for i in NUMBERS[int(k)]:
            target_value.append(i)
    frontier_start = Frontier()
    frontier_final = Frontier()
    start = Node(number)
    final = Node(target)
    frontier_start.frontier.append(start)
    frontier_final.frontier.append(final)

    explored = []
    explored_final = []
    while True:
        if len(frontier_start.frontier) == 0 or len(frontier_final.frontier) == 0:
            return "no solution"
        
        for tempnode in frontier_final.frontier:
            for node1 in frontier_start.frontier:
                if node1.number == tempnode.number:
                    return node1.action_made + tempnode.action_made

        node_start = frontier_start.remove()

        explored.append(node_start.number)
        for num in node_start.neighbour():
            if num not in explored and not frontier_start.contain(num):
                temp4 = []
                for k in str(num):
                    for n in NUMBERS[int(k)]:
                        temp4.append(n)
                child = Node(num)
                child.action_made = node_start.action_made + 1
                if numberdifference(temp4, target_value) <= 10: 
                    frontier_start.priority.append(child)
                else:
                    frontier_start.frontier.append(child)

        if len(frontier_start.frontier) == 0 or len(frontier_final.frontier) == 0:
            return "no solution"

        for tempnode in frontier_final.frontier:
            for node1 in frontier_start.frontier:
                if node1.number == tempnode.number:
                    return node1.action_made + tempnode.action_made
        
        node_final = frontier_final.remove()

        explored_final.append(node_final.number)
        for num in node_final.neighbour():
            if num not in explored and not frontier_final.contain(num):
                temp3 = []
                for k in str(num):
                    for n in NUMBERS[int(k)]:
                        temp3.append(n)
                child = Node(num)
                child.action_made = node_final.action_made + 1
                if numberdifference(temp3, number_value) <= 10: 
                    frontier_final.priority.append(child)
                else:
                    frontier_final.frontier.append(child)




if __name__ == "__main__":
    start = time.time()
    with open("2012.3a.txt") as file:
        lines = file.read()
    line = lines.split("\n")
    num1 = main(line[0])
    num2 = main(line[1])
    num3 = main(line[2])
    print(num1)
    print(num2)
    print(num3)
    end = time.time()
    print("time =",end - start)