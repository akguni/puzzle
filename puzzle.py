import re

def new_input(clue, matrix, solved):
    matrix[clue[0]][clue[1]] = clue[2]
    if clue[0] == solution[0] and clue[1] == solution[1]: return True 
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
                solved = new_input([x,clue[1],possibilities[0]], matrix, solved)

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
                solved = new_input([clue[0],y,possibilities[0]], matrix, solved)

    return solved     

while re.match()
matrix_size = int(input('Enter Matrix Size (only one number, e.g. 5): '))

matrix = [[None for i in range(matrix_size)] for j in range(matrix_size)]
print('please use 0 index throughout this program, i.e. all sequences start from 0 instead of 1')
solutionstr = input('Enter x,y coordinates of the cell to be solved, e.g. 0,0 for bottom left corner: ')
# apparently using subscriptable list is clunky as there is a more elegant way using maps
solution = [int(n) for n in solutionstr.split(',')]
print('Now please give me clues as x,y coordinates and shape number, e.g. 2,1,0 for a 0 shape in third cell right and second up from bottom left')
while True:
    cluestr = input('Enter 3 comma separated values (x,y,shape): ')
    clue = [int(n) for n in cluestr.split(',')]
    
    solved = new_input(clue, matrix, False)
    if solved:
        print(matrix[solution[0]][solution[1]])
        break