def calculate(num_a: int, num_b: int, num_c: int):
    arr = [num_a, num_b, num_c]
    most_freq_number = find_most_freq_num_in_arr(arr)

    return [find_times(most_freq_number, arr)] + sorted(remove_duplicate(arr), reverse=True)


def remove_duplicate(arr):
    return list(dict.fromkeys(arr))


def find_most_freq_num_in_arr(arr):
    return max(set(arr), key=arr.count)


def find_times(num, arr):
    sum = 0
    for i in arr:
        if i == num:
            sum += 1
    return sum
