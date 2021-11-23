import math

def main():
    list1 = [4,51,25,52,3,74,79,23,43,2,90,104,124,110]
    result = insertion(list1)
    print(result)

def insertion(list1):
    result = [list1[0]]
    list1.remove(list1[0])
    while len(list1) > 0:
        temp = list1[0]
        list1.remove(temp)
        i = 0
        while i < len(result) and temp > result[i]:
            i +=1
        result = result[:i] + [temp] + result[i:]
    return result
if __name__ == '__main__':
    main()