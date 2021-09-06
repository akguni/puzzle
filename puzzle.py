matrix_size = int(input('Enter 4 or 5 for Matrix Size: '))
matrix = [[None for i in range(matrix_size)] for j in range(matrix_size)]
solution = input('Enter x,y coordinates of the cell to be solved, e.g. 0,0 for bottom left corner: ')
# apparently using subscriptable list is clunky as there is a more elegant way using maps
solution = list(map(int, solution.split(',')))
solved = False
while solved == False:
    clue = input('Give me clues as x,y coordinates and shape number, e.g. 2,1,0 for a 0 shape in third cell right and second up from bottom left: ')
    clue = list(map(int, clue.split(',')))
    matrix[clue[0]][clue[1]]=clue[2]
 # scan the x axis using the same y coordinate as given clue
    for x in range(matrix_size):
        # process only blank cells, skip otherwise
        if matrix[x][clue[1]] == None:
            # list all possibilities first
            possibilities = [i for i in range(matrix_size)]
            # scan everything else in the same row and eliminate possibilities
            for xi in range(matrix_size):
                # scan everything else in the same column and eliminate possibilities
                for yi in range(matrix_size):
                    # only filled cells are relevant
                    if matrix[xi][yi] != None:
                        possibilities.remove(matrix[xi][yi])
                            
                    if len(possibilities) == 1:
                        matrix[x][clue[1]] = possibilities[0]
                        if x == solution[0] and clue[1] == solution[1]:
                            break


# Now do the same for y axis
 # scan the y axis using the same x coordinate as given clue
    for y in range(matrix_size):
        # process only blank cells, skip otherwise
        if matrix[clue[0]][y] == None:
            # list all possibilities first
            possibilities = [i for i in range(matrix_size)]
            # scan everything else in the same column and eliminate possibilities
            for yi in range(matrix_size):
                # scan everything else in the same row and eliminate possibilities
                for xi in range(matrix_size):
                    # only filled cells are relevant
                    if matrix[xi][yi] != None:
                        possibilities.remove(matrix[xi][yi])

                            
                    if len(possibilities) == 1:
                        matrix[clue[0]][y] = possibilities[0]
                        if y == solution[1] and clue[0] == solution[0]:
                            break



print('solution is ' + possibilities[0])