def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


# Exercise-1
input_1 = [1, 0, -1, 0, -2, 2]
target_1 = 1
output_1 = four_sum(input_1, target_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_2 = [1, 0, -1, 0, -2, 2]
target_2 = 2
output_2 = four_sum(input_2, target_2)
print(f"Exercise-2 Output: {output_2}")
