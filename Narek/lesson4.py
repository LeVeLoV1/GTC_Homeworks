"""
a = [5, 3, 6, 7, 9]
print(a)
n = int(input('введите число:'))


for elem in a:
    if n == elem:
        print('NO')
        break
    elif n != elem:
        n += n
"""

# ex_2


a = ['x', '+', '15', '-', '1', '+', '2', '=', '35']
count = 0
print(a)
for el in a:
    if 'x' in el:
        a[count], a[0] = a[0], a[count]
    elif el == '=':
        a[count], a[1] = a[1], a[count]
    count += 1
    if a[1] == '=':
        count = 2
print(a)
a.remove('x')
a.remove('=')
a[len(a) - 1], a[0] = a[0], a[len(a) - 1]
c = 0
d = 0
for i in range(1, len(a), 2):
    if i == '+':
        c = a[i - 1] - a[i + 1]
        print(c)
    elif i == '-':
        d = a[i - 1] + a[i + 1]
print(d)

print(a)
