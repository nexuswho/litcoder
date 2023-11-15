def findMaxLength(nums):
    # Create a dictionary to store the running sum and its corresponding index
    sum_indices = {0: -1}
    max_length = 0
    current_sum = 0

    for i in range(len(nums)):
        # Convert 0 to -1
        current_sum += 1 if nums[i] == 1 else -1

        # If the current sum is in the dictionary, update the max length
        if current_sum in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum])
        else:
            # If the current sum is not in the dictionary, add it with the current index
            sum_indices[current_sum] = i

    return max_length


# Exercise-1
input_nums_1 = [0, 0, 0, 1, 1, 1, 1, 0]
output_1 = findMaxLength(input_nums_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_nums_2 = [1, 0, 0, 1, 1, 1, 1, 0]
output_2 = findMaxLength(input_nums_2)
print(f"Exercise-2 Output: {output_2}")
