import numpy

def main():
    input = open("input2.txt")
    izbire = input.readline().strip().split(",")
    
    stevilke = list()
    for line in input:
        arr = line.strip().split()
        if (len(arr) >= 5):
            stevilke.append(arr)
    input.readline()
    input.close()
    prazni = [0] * (len(stevilke) // 5)
    for izbira in izbire:
        pozicija = 1
        for ind in range(0, len(stevilke), 5):
            sumOfElements = 0
            praznStolpec = [-1] * 5
            praznaVrstica = [-1] * 5
            for i in range(ind, ind+5):
                for j in range(5):
                    if (stevilke[i][j] == izbira):
                        stevilke[i][j] = -1
                    if (int(stevilke[i][j]) >= 0):
                        praznaVrstica[i%5] = 1
                        praznStolpec[j] = 1
                        sumOfElements += int(stevilke[i][j])
            sumOfElements *= int(izbira)
            sum1 = numpy.sum(praznStolpec)
            sum2 = numpy.sum(praznaVrstica)
            
            if (sum1 <= 4 or sum2 <= 4):
                prazni[ind] = -1
                if numpy.sum(prazni) == (-1* len(prazni)):
                    print(sumOfElements)
                    return
                
                
main()

    # i = 0
    # while True:
    #     vrstica = input.readline.split(" ").strip()
    #     if (len(vrstica) == 0):
    #         break
        
    #     arrays.append
    #     for j in range(1,5):
    #         vrstica = input.readline.split(" ").strip()
    #     i+=1
            