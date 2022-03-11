def main():
    input = open("kurtaga.txt")
    scores = list()
    
    for line in input:
        line = line.strip()
        vredu = True
        
        line = line.strip()
        open2close = { "(": ")", "{": "}", "[": "]", "<": ">"}
        vrsta = list()
        for char in line:
            if char in open2close:
                vrsta.append(char)
            else:
                popped = vrsta.pop()
                if (open2close[popped] != char):
                    vredu = False
                    break
                    
        if vredu:
            rezultat = 0
            char2val = { "(": 1, "{":3, "[":2, "<": 4}
            for i in range(len(vrsta)-1, 0-1, -1):
                rezultat = rezultat * 5 + char2val[vrsta[i]]
            scores.append(rezultat)
            if rezultat == 4263222782:
                print(line)
             
    scores.sort()
    # print(scores)
    print(scores[len(scores) // 2])
main()