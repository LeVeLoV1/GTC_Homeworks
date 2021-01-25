n = int(input())
q=0
m=1
while 5**m<n:
    q += n//5**m
    m += 1
print(q)