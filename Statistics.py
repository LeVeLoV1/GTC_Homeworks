def print_statistics(num_arr):
    if num_arr:
        print(len(num_arr))
        print(float(sum(num_arr) / len(num_arr)))
        print(float(min(num_arr)))
        print(float(max(num_arr)))
        print(float(num_arr[int((len(num_arr) - 1) / 2)]))
    else:
        for i in range(5):
            print(float(0))


print_statistics([22])
