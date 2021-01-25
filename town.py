n=int(input())
i=int(input())
j=int(input())

def hanoy_town(n,i,j):
    if n>0:
        hanoy_town(n-1, i ,6-1-j)
        print(i,j,sep='-', end=';')
        hanoy_town(n-1, 6-i-j,j)
    else:
        print(i,j,sep='-', end=';')

hanoy_town(n,i,j)