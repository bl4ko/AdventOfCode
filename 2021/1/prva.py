
def main():
    input = open("input.txt")
    prejsna = 0
    stevec = 0
    for line in input.readline():
        trenutna = int(line)
        if (trenutna > prejsna):
            stevec+=1
        prejsna = trenutna
    input.close()
    print(stevec)
    
main()