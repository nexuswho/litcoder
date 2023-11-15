def sliding_subarray_beauty(arr, k, n):
    beauty_list = []

    for i in range(len(arr) - k + 1):
        subarray = arr[i : i + k]
        sorted_subarray = sorted(subarray)
        beauty_list.append(sorted_subarray[n - 1])

    return beauty_list


# Exercise-1
input_arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_k_1 = 3
input_n_1 = 2
output_1 = sliding_subarray_beauty(input_arr_1, input_k_1, input_n_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_k_2 = 4
input_n_2 = 2
output_2 = sliding_subarray_beauty(input_arr_2, input_k_2, input_n_2)
print(f"Exercise-2 Output: {output_2}")
