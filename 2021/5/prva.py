import re

def main():
    input = open("input.txt")
    table = [[0 for x in range(1000)] for y in range(1000)]
    for line in input:
        line = line.replace(' -> ', ',')
        numbers = line.strip().split(',')
        for i in range(4):
            numbers[i] = int(numbers[i])
        
        x1 = numbers[0]
        y1 = numbers[1]
        x2 = numbers[2]
        y2 = numbers[3]
        if (abs(x2-x1) == abs(y2-y1)):
            if (y1 < y2):
                if (x1 < x2):
                    while (y1 <= y2):
                        table[y1][x1] += 1
                        x1 += 1
                        y1 += 1
                else:
                    while (y1 <= y2):
                        table[y1][x1] += 1
                        x1 -= 1
                        y1 += 1
            else:
                if (x1 < x2):
                    while (y1 >= y2):
                        table[y1][x1] += 1
                        x1 += 1
                        y1 -= 1
                else:
                    while (y1 >= y2):
                        table[y1][x1] += 1
                        x1 -= 1
                        y1 -= 1
                
        
        elif numbers[0] == numbers[2]: # x1 = x2
            y1 = int(min(numbers[1], numbers[3]))
            y2 = int(max(numbers[1], numbers[3]))
            x = int(numbers[0])
            while (y1 <= y2):
                table[y1][x] += 1
                y1 += 1
        elif numbers[1] == numbers[3]: # y1 = y2
            x1 = int(min(numbers[0], numbers[2]))
            x2 = int(max(numbers[0], numbers[2]))
            y = int(numbers[1])
            while (x1 <= x2):
                table[y][x1] += 1
                x1 +=1
    rez = 0
    for i in range(1000):
        for y in range(1000):
            if (table[i][y] >= 2):
                rez += 1
    print(rez)
main()