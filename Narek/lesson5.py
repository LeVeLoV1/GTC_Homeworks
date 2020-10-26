x_point = 0
o_point = 0
matrix = [[str(input()) for i in range(3)] for j in range(3)]
for elements in matrix:
    print(elements)


def cross_zero(matrix,):
    for h_el in matrix:
        for d_el in h_el:
            continue
        if not d_el:
            if h_el[0] == h_el[1] == h_el[2] == 'x' or matrix[0][0] == matrix[1][1] == matrix[2][2] == 'x' or matrix[0][2] == matrix[1][1] == matrix[2][0] == 'x' or matrix[0][0] == matrix[1][0] == matrix[2][0] == 'x' or matrix[1][0] == matrix[1][1] == matrix[1][2] == 'x' or matrix[2][0] == matrix[2][1] == matrix[2][2] == 'x':
                print('X')
                break
            elif h_el[0] == h_el[1] == h_el[2] == 'o' or matrix[0][0] == matrix[1][1] == matrix[2][2] == 'o' or matrix[0][2] == matrix[1][1] == matrix[2][0] == 'o' or matrix[0][0] == matrix[1][0] == matrix[2][0] == 'o' or matrix[1][0] == matrix[1][1] == matrix[1][2] == 'x' or matrix[2][0] == matrix[2][1] == matrix[2][2] == 'o':
                print('o')
                break
            else:
                print(-1)
                break
        else:
            global x_point
            global o_point
            if h_el == 'x':
                x_point += 1
            elif h_el == 'o':
                o_point += 1
        if x_point > o_point:
            print('ход нолика (o)')
            break
        elif x_point < o_point:
            print('ход крестика (x)')
            break

cross_zero(matrix)


