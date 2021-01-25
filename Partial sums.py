a = int(input())
def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res

print(partial_sums(0, 1, 1.5, 1.75, 1.875))