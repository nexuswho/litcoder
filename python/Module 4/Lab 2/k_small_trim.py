def kth_smallest_trimmed_number(nums, queries):
    answer = []

    for query in queries:
        position, trim = query
        trimmed_nums = [int(num[-trim:]) for num in nums]
        sorted_indices = sorted(
            range(len(trimmed_nums)), key=lambda x: (trimmed_nums[x], x)
        )
        kth_smallest_index = sorted_indices[position - 1]
        answer.append(kth_smallest_index)

    return answer


# Exercise-1
input_nums_1 = ["113", "933", "231", "719"]
input_queries_1 = [[1, 1], [2, 2], [4, 2], [1, 3]]
output_1 = kth_smallest_trimmed_number(input_nums_1, input_queries_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_nums_2 = ["123", "456", "246", "369"]
input_queries_2 = [[1, 1], [2, 2], [4, 2], [1, 3]]
output_2 = kth_smallest_trimmed_number(input_nums_2, input_queries_2)
print(f"Exercise-2 Output: {output_2}")
