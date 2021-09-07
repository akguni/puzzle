def new_input(clue, matrix):
    matrix[clue[0]][clue[1]] = clue[2]
 # scan the x axis using the same y coordinate as given clue
    for x in range(matrix_size):
        # process only blank cells, skip otherwise
        if matrix[x][clue[1]] == None:
            # list all possibilities first
            possibilities = [i for i in range(matrix_size)]
            # scan everything else in the same row/column and eliminate possibilities
            for xi in range(matrix_size):
                if matrix[xi][clue[1]] in possibilities:
                    possibilities.remove(matrix[xi][clue[1]])
            for yi in range(matrix_size):
                if matrix[x][yi] in possibilities:
                    possibilities.remove(matrix[x][yi])
            if len(possibilities) == 1:
                matrix[x][clue[1]] = possibilities[0]
                new_input([x,clue[1],matrix[x][clue[1]]], matrix)

    for y in range(matrix_size):
    # process only blank cells, skip otherwise
        if matrix[clue[0]][y] == None:
            # list all possibilities first
            possibilities = [i for i in range(matrix_size)]
            # scan everything else in the same row/column and eliminate possibilities
            for xi in range(matrix_size):
                if matrix[xi][y] in possibilities:
                    possibilities.remove(matrix[xi][y])
            for yi in range(matrix_size):
                if matrix[clue[0]][yi] in possibilities:
                    possibilities.remove(matrix[clue[0]][yi])
            if len(possibilities) == 1:
                matrix[clue[0]][y] = possibilities[0]
                new_input([clue[0],y,matrix[clue[0]][y]], matrix)


matrix_size = int(input('Enter 4 or 5 for Matrix Size: '))
matrix = [[None for i in range(matrix_size)] for j in range(matrix_size)]
solutionstr = input('Enter x,y coordinates of the cell to be solved, e.g. 0,0 for bottom left corner: ')
# apparently using subscriptable list is clunky as there is a more elegant way using maps
solution = [int(n) for n in solutionstr.split(',')]
solved = False
while solved == False:
    cluestr = input('Give me clues as x,y coordinates and shape number, e.g. 2,1,0 for a 0 shape in third cell right and second up from bottom left: ')
    clue = [int(n) for n in cluestr.split(',')]
    matrix[clue[0]][clue[1]] = clue[2]
    new_input(clue, matrix)
    if matrix[solution[0]][solution[1]]: solved = True

print('solution is ' + possibilities[0])

