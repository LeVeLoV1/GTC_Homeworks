text = input()
def space_game(text):
    print(text)
    text = text.split()
    l = len(text)
    print(l)
    if l % 2 == 0:
        print("Выиграли")
    else:
        print("проиграли")