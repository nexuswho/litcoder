def clumsy_factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 7

    result = n * (n - 1) // (n - 2) + (n - 3)
    n -= 4

    while n >= 4:
        result -= n * (n - 1) // (n - 2) - (n - 3)
        n -= 4

    return result - clumsy_factorial(n)


# Exercise-1
input_n_1 = 5
output_1 = clumsy_factorial(input_n_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_n_2 = 10
output_2 = clumsy_factorial(input_n_2)
print(f"Exercise-2 Output: {output_2}")
