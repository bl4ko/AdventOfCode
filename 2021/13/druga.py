import copy

global_score = 0
def main():
    input = open("input.txt")
    zacetek = list()
    konec = list()
    char2pair = dict()
    
    for line in input:
        besede = line.strip().split("-")
        if besede[0] == "start":
            zacetek.append(besede[1])
            if besede[1] not in char2pair:
                char2pair[besede[1]] = []
        elif besede[1] == "start":
            zacetek.append(besede[0])
            if besede[0] not in char2pair:
                char2pair[besede[0]] = []
        elif besede[1] == "end":
            konec.append(besede[0])
        elif besede[0] == "end":
            konec.append(besede[1])
        else:
            dictAdd(besede[0], besede[1], char2pair)
            dictAdd(besede[1], besede[0], char2pair)
    
    global global_score
    for i in range(len(zacetek)):
        recursion(zacetek[i], konec, copy.deepcopy(char2pair), zacetek[i], False)
    print(global_score)
    
def recursion(startChar, endingChars, dict, StringBuilder, bonus):
    
    if startChar in endingChars:
        global global_score
        global_score += 1
        
    moznosti = dict[startChar]
    # ce je mejhna jama jo zbrisemo
    if startChar.islower():
        distinctChars = {}
        if StringBuilder.count(startChar) == 2:
            for char in StringBuilder:
                if char.islower():
                    odstraniNode(char, dict)
                    if char in moznosti:
                        moznosti.remove(char)
            bonus = True
        
        if (bonus):
            odstraniNode(startChar, dict)
            
    for moznost in moznosti:
        recursion(moznost, endingChars, copy.deepcopy(dict), StringBuilder + moznost, bonus)
    
def odstraniNode(startChar, dict):
    if startChar in dict:
        del dict[startChar]
        for key in dict:
            if startChar in dict[key]:
                dict[key].remove(startChar)
    
def preveriSosede(startChar, dict):
    for i in dict[startChar]:
        if i in dict:
            return True
    return False

def dictAdd(char1, char2, char2pair):
    if char1 not in char2pair:
        char2pair[char1] = [char2]
    else:
        char2pair[char1].append(char2)
     
main()