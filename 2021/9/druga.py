# ccff = 1
def main():
    input = open("kurtaga.txt")
    t = list()
    for line in input:
        vrstica = list()
        for char in line.strip():
            vrstica.append(int(char))
        t.append(vrstica)
    
    basins = [1,1,1]
    memo = [[0 for x in range(len(t[0]))] for y in range(len(t))]
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 9 and memo[i][j] == 0:
                result = recursion(i, j, memo, t)
                if basins[0] < result:
                    basins[0] = result
                    basins.sort()
    
    print(basins)
    print(basins[0] * basins[1] * basins[2])
    
# preskeniramo obmocje omejeno z 9kami
def recursion(i, j, memo, t):
    if i < 0 or j < 0 or i >= len(t) or j >= len(t[0]):
        return 0
    if memo[i][j] == 1 or t[i][j] == 9:
        return 0
    memo[i][j] = 1
    return 1 + recursion(i-1, j, memo, t) + recursion(i+1, j, memo, t) + recursion(i, j-1, memo, t) + recursion(i, j+1, memo, t)
    
main()