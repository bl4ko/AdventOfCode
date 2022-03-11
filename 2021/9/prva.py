# ccff = 1
def main():
    input = open("input2.txt")
    doubleArr = list()
    for line in input:
        vrstica = list()
        for char in line.strip():
            vrstica.append(int(char))
        doubleArr.append(vrstica)
    
    result = 0
    for i in range(len(doubleArr)):
        for j in range(len(doubleArr[0])):
            kandidat = int(doubleArr[i][j])
            # pogledamo vse 4 moznosti
            if (i-1 >= 0 and doubleArr[i-1][j] <= kandidat):
                continue
            if (i+1 < len(doubleArr) and doubleArr[i+1][j] <= kandidat):
                continue
            if (j-1 >= 0 and doubleArr[i][j-1] <= kandidat):
                continue
            if (j+1 < len(doubleArr[i]) and doubleArr[i][j+1] <= kandidat):
                continue
            result += kandidat + 1
    print(result)
main()