import thread


def main():
    input = open("input2.txt")
    zacetek = input.readline().strip().split(",")
    memo = [0] * 10
    for i in range(len(zacetek)):
        zacetek[i] = int(zacetek[i])
    vsota = 0
    for i in range(len(zacetek)):
        if memo[zacetek[i]] == 0:
            stUstvarjenih(zacetek[i], 256, memo)
        vsota += memo[zacetek[i]]
    print(vsota)
    
    
def stUstvarjenih(prvihDni, dni, memo):
    zacetek = list()
    zacetek.append(prvihDni)
    for i in range(dni):
        for j in range(len(zacetek)):
            zacetek[j] -= 1
            if (zacetek[j] == -1):
                zacetek[j] = 6
                zacetek.append(8)
    print(len(zacetek))
    memo[prvihDni] = len(zacetek) 
    print(memo)
main()