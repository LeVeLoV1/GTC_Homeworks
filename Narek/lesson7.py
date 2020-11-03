list_nums = [2, -1, 1, 5, 4, -1, 3]
print('list =', list_nums)
rememb = []
count = 0

for el in list_nums:
    if el == -1:
        rememb.append(count)
        del list_nums[count]
    count += 1
result = sorted(list_nums)

for rem_nums in rememb:
    result.insert(rem_nums, -1)

print(result)







