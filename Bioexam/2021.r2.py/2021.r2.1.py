import copy


VALUES = ["A", "B"]

def main():

    number = int(input("number: "))
    max = number
    groups = []
    for i in range(number // 2):
        temp = input("pair: ").split(" ")
        x = temp[0]
        y = temp[1]
        groups.append((x, y))
    assignment = {}
    result = backtrack(assignment, max, 0, groups)
    result = sorted(result.items(), key=lambda item: item[0])
    string = ""
    for value in result:
        string += str(value[1])
    print(string)

def backtrack(assignment, max, position, groups):
    if len(assignment) == max:
        return assignment
    var = select_unassigned(assignment, position)
    for value in VALUES:
        newassignment = copy.deepcopy(assignment)
        newassignment[var] = value
        newassignment = inference(newassignment, var, value, groups)
        if consistent(newassignment, max, groups):
            result = backtrack(newassignment, max, position, groups)
            if result is not None:
                return result
    return None



def select_unassigned(assignment, position):
    while True:
        if position in assignment.keys():
            position += 1
        else:
            return position

def consistent(assignment, max, groups):
    keys = []
    assignment = sorted(assignment.items(), key=lambda item: item[0])
    values = []
    for k in assignment:
        keys.append(k[0])
        values.append(k[1])
    for x, y in groups:
        x = int(x)
        y = int(y)
        try:
            if x in keys and y in keys:
                if assignment[x][1] == assignment[y][1]:
                    return False
        except IndexError:
            pass
    for i in range(max - 2):
        count = 0
        try:
            if keys[i]  + 1 == keys[i+1] and keys[i + 1] + 1 == keys[i + 2]:
                if values[i] == values[i + 1] and values[i + 1] == values[i+2]:
                    return False
        except IndexError:
            pass
        try:
            if keys[i]  + 1 == keys[i+1] and keys[i + 1] + 1 == keys[i + 2] and keys[i + 2]  + 1 == keys[i+ 3] and keys[i + 3] + 1 == keys[i + 4]:
                for j in range(i, i +5):
                    if values[j] == "A":
                        count+= 1
                if count != 2 and count != 3:
                    return False
        except IndexError:
            pass
    return True


def inference(assignment, var, value, groups):
    for x, y in groups:
        if var == x:
            if y not in assignment.keys():
                if value == "A":
                    assignment[y] = "B"
                else:
                    assignment[y] = "A"
        elif var == y:
                if x not in assignment.keys():
                    if value == "A":
                        assignment[x] = "B"
                    else:
                        assignment[x] = "A"

    return assignment


if __name__ == "__main__":
    main()