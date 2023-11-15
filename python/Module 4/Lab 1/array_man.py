def mix_the_array(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        start, end, value = query
        arr[start] += value
        if end + 1 <= n:
            arr[end + 1] -= value

    max_value = 0
    current_value = 0

    for i in range(1, n + 1):
        current_value += arr[i]
        max_value = max(max_value, current_value)

    return max_value


# Exercise-1
input_n_1 = 5
input_queries_1 = [[2, 4, 3], [4, 5, 9], [3, 3, 11]]
output_1 = mix_the_array(input_n_1, input_queries_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_n_2 = 10
input_queries_2 = [[3, 10, 3], [4, 5, 9], [2, 9, 11]]
output_2 = mix_the_array(input_n_2, input_queries_2)
print(f"Exercise-2 Output: {output_2}")
