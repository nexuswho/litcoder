def count_zero_filled_subarrays(nums):
    count = 0  # Counter for consecutive zeros
    result = 0  # Total count of zero-filled subarrays

    for num in nums:
        if num == 0:
            count += 1
        else:
            result += (count * (count + 1)) // 2
            count = 0

    # Add the count for the last group of consecutive zeros (if any)
    result += (count * (count + 1)) // 2

    return result


# Exercise-1
nums_1 = [1, 2, 0, 0, 0]
output_1 = count_zero_filled_subarrays(nums_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
nums_2 = [1, 0, 0, 2, 0, 3, 0]
output_2 = count_zero_filled_subarrays(nums_2)
print(f"Exercise-2 Output: {output_2}")
