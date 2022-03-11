def main():
    input = open("input.txt")
    povprecni = [0]*12
    for line in input:
        binary = line.strip()
        for i in range(0,12):
            if binary[i] == '0':
                povprecni[i] -= 1
            else:
                povprecni[i] += 1
    input.close()
    rez = ""
    xorrez = ""
    for i in range(12):
        if povprecni[i] < 0:
            rez += '0'
            xorrez += '1'
        else:
            rez += '1'
            xorrez += '0'
    print(int(rez,2) * int(xorrez,2))
main()