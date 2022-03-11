from heapq import heappush, heappop, heapify # importamo kopico (tako naredimo priority queue)

def main():    
    matrix = readInput("input2.txt")
    global LENx, LENy
    LENy = len(matrix)
    LENx = len(matrix[0])
    shortest = dijkstra((0,0), (LENy, LENx), matrix)
    print(shortest)
    
def readInput(fileName):
    input = open(fileName)
    matrix = list()
    for line in input:
        matrixLine = list()
        for char in line.strip():
            matrixLine.append(int(char))
        matrix.append(matrixLine)
    return matrix
    
def adjacentList(terka):
    adjacentNodes = list()
    if terka[0]-1 >= 0: adjacentNodes.append((terka[0]-1, terka[1]))
    if terka[0]+1 < LENy: adjacentNodes.append((terka[0]+1, terka[1]))
    if terka[1]-1 >= 0: adjacentNodes.append((terka[0], terka[1]-1))
    if terka[1]+1 < LENx: adjacentNodes.append((terka[0], terka[1]+1))
    return adjacentNodes

# Dijkstra algorithm
def dijkstra(start, end, matrix):
    # Inicializeramo kopico: (shranjevali bomo koordinate nodov)
    heap = []; heapify(heap)
    # Na zacetku dodamo v kopico zacetno vozlisce (priority, oznaka, precessor)
    heappush(heap, start) 
    while (len(heap) > 0):
        # Poberemo koren iz kopice, to vozlisce dodamo v vpeto drevo:
        currNode = heappop(heap)
        # Nadaljujemo z pregledom njegovih naslednikov
        # Sprehodimo se cez naslednike (ni pomembno v katerem vrstnem redu)
        adjacentNodes = adjacentList(currNode)
        for adjacentNode in adjacentNodes:
            print(adjacentNode)
    
    return -1
    
main()