first = list(input())
second = list(input())

letters = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in range(1, 9):
    if letters[i] == first[0]:
        if (i + int(first[1])) % 2 == 0:
            first = 'black'
        else:
            first = 'white'

# second position
    if letters[i] == second[0]:
        if (i + int(second[1])) % 2 == 0:
            second = 'black'
        else:
            second = 'white'

print(second == first)
