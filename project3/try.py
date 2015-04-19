__author__ = 'imaclab22'

line= '...9....2.5.1234...3....16.9.8.......7.....9.......2.5.91....5...7439.2.4....7...'
matrix = []
for i in range(9):
    temp = []
    for j in range(9):
        h = i*9+j
        if line[h]=='.':
            temp.append(None)
        else:
            temp.append(int(line[h]))
    matrix.append(temp)


rVal = ''
for i in range(9):
    if i > 0 and i % 3 == 0:
        rVal += 21* '-' + '\n'
    for j in range(9):
        if j > 0 and j % 3 == 0:
            rVal += '| '
        if matrix[i][j] == None:
            rVal += '. '
        else:
            rVal += str(matrix[i][j]) + ' '
    if i != 8:
        rVal += '\n'
print rVal