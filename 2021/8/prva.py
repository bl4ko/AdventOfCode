# ccff = 1
def main():
    input = open("input.txt")
    konec = 0
    for line in input:
        dict = {2: "", 4: "", 3: "", 7: ""}
        data = line.strip().split()
        inputCrke = [data[i] for i in range(0, 10)]
        outputCrke = [data[i] for i in range(11, 15)]
        for beseda in inputCrke:
            if len(beseda) in dict:
                dict[len(beseda)] = beseda
        
        result = ""
        for beseda in outputCrke:
            if (len(beseda) == 2):
                result += "1"
            elif (len(beseda) == 4):
                result += "4"
            elif (len(beseda) == 3):
                result += "7"
            elif (len(beseda) == 7):
                result += "8"
            elif (len(beseda) == 6):
                # 0, 6, 9
                ostalaCrka = "".join(set(dict[7]) - set(beseda))
                if ostalaCrka in dict[2]:
                    result += "6"
                elif ostalaCrka in dict[4]:
                    result += "0"
                else:
                    result += "9"
            elif (len(beseda) == 5):
                # 2, 3 ,5
                ostaliCrki = set(dict[7]) - set(beseda)
                if (len(ostaliCrki - set(dict[4])) == 0):
                    result += "2"
                elif (len(ostaliCrki - set(dict[3])) == 1):
                    result += "5"
                else:
                    result += "3"
        konec += int(result)
    print(konec)
main()