# Ex 1
sentence = input()
punct = (',', '.', ';', ':', '!', '?', '"', "'")

for i in range(len(punct)):
    sentence = sentence.replace(punct[i], "")
print(sentence)

# Ex 2
number = input()
print(round(sum(list(map(int, number))) / len(number), 1))

# Ex 3
sentence2 = input()
score_upper, score_lower = 0, 0

for elem in sentence2:
    if elem.isupper():
        score_upper += 1
    elif elem.isalpha():
        score_lower += 1
print('У вас', score_lower, 'строчных букв и', score_upper, 'заглавних')

# Ex 4
var_name = input()

for words in var_name:
    if not words.isalnum() and words != '_':
        print('эти знаки не могут использоваться в имени переменного')
        break
    elif var_name[0].isnumeric():
        print('первый символ имени переменного не может быть цифрой')
        break
    else:
        print('successful')
        break
