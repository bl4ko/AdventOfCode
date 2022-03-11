import copy



# NNCB
# NN -> C
# NCNCB
# NC -> B
# N
# CB -> H
# NBCNBHCB

def main():
    input = open("input.txt")
    template = input.readline().strip()
    input.readline()
    rules = dict()
    for line in input:
        besede = line.strip().split(" ")
        rules[besede[0]] = besede[2]
    
    steps = 40
    for i in range(steps):
        # sprehodimo se cez template
        st_vstavitev = 0
        novi_template = template
        for j in range(len(template)-1):
            if template[j:j+2] in rules:
                novi_template = novi_template[:j+1+st_vstavitev] + rules[template[j:j+2]] +novi_template[j+1+st_vstavitev:]
                st_vstavitev += 1
        template = novi_template
    
    max_count = 0
    min_count = 0
    for char in rules.values():
        occurances = template.count(char)
        if occurances > max_count or max_count == 0:
            max_count = occurances
        if occurances < min_count or min_count == 0:
            min_count = occurances
    print(max_count - min_count)
    
main()