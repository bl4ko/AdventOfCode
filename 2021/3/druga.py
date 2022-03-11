def main():
    input = open("input2.txt")
    besede = list()
    for line in input:
        besede.append(line.strip())
    input.close()
    besede2 = besede.copy()
    print(substance(besede, "+") * substance(besede2, "-"))

def substance(arr, opr):
    for i in range(len(arr[0])):
        if (len(arr) == 1):
            break
        povprecni = 0
        for beseda in arr:
            if beseda[i] == '0':
                povprecni -= 1
            else:
                povprecni += 1
        if povprecni >= 0:
            povprecni = 0 if opr == "-" else 1
        else:
            povprecni = 1 if opr == "-" else 0    
        for j in range(len(arr)-1, -1, -1):
            if arr[j][i] != str(povprecni):
                arr.remove(arr[j])
    oxy = int(arr[0], 2)
    return oxy
    # 1327
    # 3429
main()