def who_are_you_and_hello():
    y = True
    x = input()
    while y:
        if x.isalpha() and x[0].istitle() and x[1:].islower():
            y = False
        else:
            x = input()
    print('Привет, ', x, '!', sep='')


who_are_you_and_hello()
