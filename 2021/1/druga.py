def main():
    input = open("input.txt")
    queue = []
    st_branj = 0 
    prejsna = 0
    stevec = 0
    for line in input:
        if (st_branj >= 3):
            trenutna = int(line)
            queue.append(trenutna)
            prejsni = queue.pop(0)
            
            if (trenutna > prejsni):
                stevec+=1
                # print(str(prejsni) + " " + str(trenutna))
        else:
            prejsna += int(line)
            queue.append(prejsna)
            st_branj += 1
    input.close()
    print(stevec)
main()