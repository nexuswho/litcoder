def min_set_size(num, k):
    if num % 10 == k:
        return 1
    elif (num % 2 == 0) and (k % 2 == 0):
        return 2
    elif (num % 2 == 1) and (k % 2 == 1):
        return 2
    elif (num % 2 == 0) and (k % 2 == 1):
        return 4
    else:
        return -1


# Exercise-1
num1 = 56
k1 = 9
output_1 = min_set_size(num1, k1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
num2 = 53
output_2 = min_set_size(num2, k1)
print(f"Exercise-2 Output: {output_2}")
