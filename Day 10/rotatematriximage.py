# Rotate a given matrix 
def rotatematrix(matrix):
    for i in range(1,len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[j][i]
    for i in range(len(matrix)):
        matrix[i]= matrix[i][::-1]
    
result = rotatematrix([[1,2,3],[4,5,6],[7,8,9]])
print(result)