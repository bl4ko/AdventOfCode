def main():
    input = open("input2.txt")
    matrix = list()
    

    for line in input:
        line = line.strip()
        vrstica = list()
        for char in line:
            vrstica.append(int(char))
        matrix.append(vrstica)
   
    
    
    for i in range(1000000):
        result = 0    
        memo = [[0 for i in range(10)] for j in range(10)]
        for j in range(10):
            for k in range(10):
                matrix[j][k] += 1
                
        for j in range(10):
            for k in range(10):
                if matrix[j][k] > 9:
                    povecajOstale(j, k, matrix, memo)
                
        
        for j in range(10):
            for k in range(10):
                if matrix[j][k] > 9:
                    result += 1
                    matrix[j][k] = 0
        
        if (result == 100):
            print(i)
            return
        
        # print("step %d, %d" % (i, result))
        # for line in matrix:
        #     print(line)
    
        
        

def povecajOstale(i, j, matrix, memo):
    if (memo[i][j] == 1):
        return
    memo[i][j] = 1
    if (i-1 >= 0):
        matrix[i-1][j] += 1
        if (matrix[i-1][j] > 9): povecajOstale(i-1, j, matrix, memo)
        
        if (j-1 >= 0):
            matrix[i-1][j-1] += 1
            if (matrix[i-1][j-1] > 9): povecajOstale(i-1, j-1, matrix, memo)
            
        if (j+1 < len(matrix[0])):
            matrix[i-1][j+1] += 1
            if (matrix[i-1][j+1] > 9): povecajOstale(i-1, j+1, matrix, memo)
            
    if (i+1 < len(matrix)):
        matrix[i+1][j] += 1
        if (matrix[i+1][j] > 9): povecajOstale(i+1, j, matrix, memo)
        
        if (j-1 >= 0):
            matrix[i+1][j-1] += 1
            if (matrix[i+1][j-1] > 9): povecajOstale(i+1, j-1, matrix, memo)
            
        if (j+1 < len(matrix[0])):
            matrix[i+1][j+1] += 1
            if (matrix[i+1][j+1] > 9): povecajOstale(i+1, j+1, matrix, memo)
    
    if (j+1 < len(matrix)):
        matrix[i][j+1] += 1
        if (matrix[i][j+1] > 9): povecajOstale(i, j+1, matrix, memo)
    if (j-1 >= 0):
        matrix[i][j-1] +=1
        if (matrix[i][j-1] > 9): povecajOstale(i, j-1, matrix, memo)
    
         
main()