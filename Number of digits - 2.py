number = list(input())


def num_digits(n):
    conutik = 0
    for i in number:
        if not i:
            return '0'
        else:
            conutik += 1
            
    return conutik


print(num_digits(number))