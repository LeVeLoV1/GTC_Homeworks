xcord = float(input())
ycord = float(input())


def quarter(xcord_, ycord_):
    if xcord_ > 0 and ycord_ > 0:
        print('1 quarter')
    elif xcord_ < 0 < ycord_:
        print('2 quarter')
    elif xcord_ < 0 and ycord_ < 0:
        print('3 quarter')
    elif xcord_ > 0 > ycord_:
        print('4 quarter')
    elif xcord_ == 0 or ycord_ == 0:
        print('нельзя вводить 0')


quarter(3, 4)
