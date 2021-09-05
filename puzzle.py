matrix_size = int(input('Enter 4 or 5 for Matrix Size: '))
matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
solution = input('Enter x,y coordinates of the cell to be solved, e.g. 0,0 for bottom left corner: ')
solved = False
while solved == False:
    clue = input('Give me clues as x,y coordinates and shape number, e.g. 2,1,0 for a 0 shape in third cell right and second up from bottom left: ').split(',')
    matrix[int(clue[0])][int(clue[1])]=int(clue[2])
