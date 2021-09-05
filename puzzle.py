matrix_size = int(input('Enter 4 or 5 for Matrix Size: '))
matrix = [[None for i in range(matrix_size)] for j in range(matrix_size)]
solution = input('Enter x,y coordinates of the cell to be solved, e.g. 0,0 for bottom left corner: ').split(',')
solved = False
while solved == False:
    clue = input('Give me clues as x,y coordinates and shape number, e.g. 2,1,0 for a 0 shape in third cell right and second up from bottom left: ').split(',')
    matrix[int(clue[0])][int(clue[1])]=int(clue[2])
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == None:
                possibilities = [x for x in range(matrix_size)]
                for l in range(matrix_size):
                    for m in range(matrix_size):
                        if matrix[l][m] != None:
                            if l == i or j == j:
                                possibilities.remove(matrix[l][m])                
            if len(possibilities) == 1:
                matrix[i][j] = possibilities[0]
                if i == int(solution[0]) and j == int(solution[1]):
                    break
    

print('solution is ' + possibilities[0])