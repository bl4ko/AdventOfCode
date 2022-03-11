def main():
    input = open("input2.txt")
    povprecni = [0]*5
    for line in input:
        besede = line.strip()
        # gamma rate most common each bit
        # print(povprecni)
        # print(besede)
        for i in range(0,5):
            if besede[i] == '0':
                povprecni[i] -= 1
            else:
                povprecni[i] += 1
    rez = ""
    rez2 = ""
    for i in range(5):
        if povprecni[i] < 0:
            rez += '0'
            rez2 += '1'
        else:
            rez += '1'
            rez2 += '0'
        print("rez = " + rez)
    
    print(int(rez,2) * int(rez2,2))
    input.close()
main()