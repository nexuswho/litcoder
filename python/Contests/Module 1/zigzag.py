def zigzag_sequence(n, arr):
    arr.sort()
    first_half = arr[: n // 2]
    second_half = arr[n // 2 :][::-1]

    result = []
    for i in range(n // 2):
        result.append(first_half[i])
        result.append(second_half[i])

    if n % 2 != 0:
        result.append(first_half[-1])

    return result


# Exercise-1
input_n_1 = 5
input_arr_1 = [2, 6, 8, 4, 10]
output_1 = zigzag_sequence(input_n_1, input_arr_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_n_2 = 7
input_arr_2 = [7, 6, 8, 15, 9, 3, 1]
output_2 = zigzag_sequence(input_n_2, input_arr_2)
print(f"Exercise-2 Output: {output_2}")
