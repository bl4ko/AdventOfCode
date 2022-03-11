import copy

def main():
    input = open("input.txt")
    template = input.readline().strip()
    input.readline()
    rules = dict()
    char2occurances = dict()
    for line in input:
        besede = line.strip().split(" ")
        rules[besede[0]] = besede[2]
        char2occurances[besede[2]] = 0
    
    pairs = dict()
    for i in range(0, len(template)):
        if (i <= len(template)-2):
            if template[i:i+2] in pairs:
                pairs[template[i:i+2]] += 1
            else:
                pairs[template[i:i+2]] = 1
        if template[i] in char2occurances:
            char2occurances[template[i]] += 1
        else:
            char2occurances[template[i]] = 0
            
    steps = 40
    for i in range(steps):
        new_pairs = dict(pairs)
        for key in pairs:
            if key in rules:
                # razbitje v 2 nova para
                nova_para = [key[0]+rules[key], rules[key]+key[1]] 
                char2occurances[rules[key]] += pairs[key]
                stNovih = pairs[key]
                new_pairs[key] -= pairs[key]
                if nova_para[0] in new_pairs:
                    new_pairs[nova_para[0]] += stNovih
                else:
                    new_pairs[nova_para[0]] = stNovih
                if nova_para[1] in new_pairs:
                    new_pairs[nova_para[1]] += stNovih
                else:
                    new_pairs[nova_para[1]] = stNovih
                if (new_pairs[key] <= 0):
                    del new_pairs[key]
        pairs = new_pairs

    print(max(list(char2occurances.values()))-min(list(char2occurances.values())))
    
main()