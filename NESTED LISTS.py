a = []
sta, stb = int(input()), int(input())
for i in range(sta):
    b = []
    for j in range(stb):
        b.append(input())
    a.append(b)
for i in a:
    for j in range(stb - 1):
        print(i[j], end='\t')
    print(i[-1])
print()

