def main():
    input = open("input.txt")
    positions = [0] * 2
    positions[0] = int(input.readline().strip().split(" ")[4]) - 1
    positions[1] = int(input.readline().strip().split(" ")[4]) - 1 
    
    onTurn = 0 # which player is on turn (0 or 1)
    scores = [0] * 2 # scores[0] = score for player 0, scores[1] = score for player 1
    

    medStep = 2 # median of three numbers rolled (1 _2_ 3 in first case)
    rolls = 0 # number of all rolls
    while scores[0] < 1000 and scores[1] < 1000:
        updatePosition(medStep, onTurn, positions)
        updateScore(onTurn, positions, scores)
        
        onTurn = updateOnTurn(onTurn)   
        rolls += 3
        medStep += 3
        # print("[%d]: %d, numOfRolls=%d" % (onTurn, scores[onTurn], rolls))
        
        # robni pogoji
        if medStep >= 100:
            if medStep == 100:
                medStep = 3
                # naslednemu igralcu pristejemo 200
                positions[onTurn] += 200
                positions[onTurn] %= 10
                rolls += 3
                updateScore(onTurn, positions, scores)
                onTurn = updateOnTurn(onTurn)
                
                
                
            elif medStep == 101:
                medStep = 4
                # naslednemu igralcu pristejemo 103
                positions[onTurn] += 103
                positions[onTurn] %= 10
                rolls += 3
                updateScore(onTurn, positions, scores)
                onTurn = updateOnTurn(onTurn)
                
            elif medStep == 102: # normalno
                medStep = 2  
        
    print(min(scores) * rolls)

def updateOnTurn(onTurn):
    return (onTurn+1) % 2

def updatePosition(medStep, onTurn, positions):
    positions[onTurn] += medStep * 3
    positions[onTurn] %= 10

def updateScore(onTurn, positions, scores):
    scores[onTurn] += positions[onTurn] + 1 # [0,9] -> [1,10]


main()