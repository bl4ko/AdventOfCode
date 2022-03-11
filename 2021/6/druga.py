def main():
    input = open("input.txt")
    nums = [int(x) for x in input.readline().strip().split(",")]

    slovar = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for num in nums:
        slovar[num] += 1
    
    stDni = 256
    slovar[8] = 0
    for i in range(stDni):
        novSlovar = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        keys = slovar.keys()
        for key in keys:
            stRib = slovar[key]
            key -= 1
            if (key == -1):
                novSlovar[8] += stRib
                novSlovar[6] += stRib
            else:
                novSlovar[key] += stRib
        slovar = novSlovar
    print(sum(slovar.values()))

main()