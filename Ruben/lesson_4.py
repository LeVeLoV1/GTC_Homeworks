# Minesweeper

length, height = int(input('введите длину матрицы:')), int(input('введите высоту матрицы:'))
matrix = [[bool(input('если в этой ячейке нет мин нажмите "Enter" ')) for i in range(length)] for j in range(height)]

for elements in matrix:
    print(elements)

    if elements:
        elements = 1
        print(elements)
    elif not elements:
        elements = 2
        print(elements)





'''


mines = []
while len(mines) != K:
  coords = input().split()
  if len(coords) == 2 and all(map(str.isdigit, coords)):
        coords = tuple(map(int, coords))
        if all(map(lambda x: x > 0, coords)):
            mines.append(coords)
                    
def Mines(a, b):
  return sum((i, j) in mines for i, j in Pole(a, b))
  
for i in range(N):
  for j in range(M):
    if (i, j) not in mines:
      print(Mines(i, j), end=' ')
    else:
      print('b', end=' ')
  print()
'''



# ex 2