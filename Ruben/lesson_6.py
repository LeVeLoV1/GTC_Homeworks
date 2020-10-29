position = list(input())
letters = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def possible_turns(cell):

    for i in range(1, 9):
        if letters[i] == position[0]:
            for Y1 in range(1, 9):
                for Y2 in range(1, 9):
                    x1 = i
                    x2 = int(cell[1])
                    y1 = Y1
                    y2 = Y2
                    dx = abs(int(x1 - x2))
                    dy = abs(int(y1 - y2))
                    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                        print(letters[Y1], Y2)


possible_turns(position)
