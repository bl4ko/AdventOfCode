import copy


def main():
    # inicializacija matrike
    maxX = 0
    maxY = 0
    input = open("input.txt")
    vrednosti = list()
    for line in input:
        if (line == "\n"): break
        nums = [int(x) for x in line.strip().split(",")]
        vrednosti.append((nums[1], nums[0]))
        if (nums[1] > maxX):
            maxX = nums[1]
        if (nums[0] > maxY):
            maxY = nums[0]
    matrix = [[0 for i in range(maxY+1)] for j in range(maxX+1)]
    for terka in vrednosti: 
        matrix[terka[0]][terka[1]] = 1
    # konec inicializacije matrike
    
    # branje foldov
    for line in input:
        besede = line.strip().split()
        besede = besede[2].split("=")
        if besede[0] == "x":
            foldX(int(besede[1]), matrix)
        else:
            foldY(int(besede[1]), matrix)
    printM(matrix)
    
def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                print("#", end='')
            else:
                print(" ", end='')
        print()
        
def foldX(x, matrix):
    for i in range(0, len(matrix)):
        nova_vrstica = x-1
        for j in range(x+1, len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][nova_vrstica] = 1
            nova_vrstica -= 1   
    for i in range(len(matrix)):
        matrix[i] = matrix[i][0:x]
      
def foldY(y, matrix):
    # po vrsticah
    nova_vrstica = y-1
    for i in range(y+1, len(matrix)):
        for j in range(len(matrix[y])):
            if matrix[i][j] == 1:
                matrix[nova_vrstica][j] = 1
        nova_vrstica -= 1
        
    for i in range(len(matrix)-1, y-1, -1):
        matrix.pop(i)
    
main()