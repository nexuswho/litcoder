def last_remaining(n):
    start, step, direction = 1, 2, 1
    while n > 1:
        start += direction * (step * (n // 2) - step // 2)
        n //= 2
        step *= 2
        direction *= -1
    return start


# Exercise-1
input_1 = 10
output_1 = last_remaining(input_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_2 = 100
output_2 = last_remaining(input_2)
print(f"Exercise-2 Output: {output_2}")
