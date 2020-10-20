def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    print(m2)


stu_connt = int(input())
information = []
names = []
appraisals = []

for i in range(stu_connt):
    name = input()
    names.append(name)

    appraisal = int(input())
    appraisals.append(appraisal)

    information.append([name, appraisal])

second_smallest(appraisals)  # преднаименьшое число
print(sorted(names))  # сортировка по алфавитному порядку

print("")
print(appraisals)
print(names)
print(information)