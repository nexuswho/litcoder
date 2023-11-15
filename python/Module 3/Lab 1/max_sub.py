def maximize_subsequences(text, pattern):
    count_pattern_0 = text.count(pattern[0])
    count_pattern_1 = text.count(pattern[1])

    # Option 1: Add pattern[0] at any position
    count_0 = text.count(pattern)
    count_0 += count_pattern_1 * len(pattern)

    # Option 2: Add pattern[1] at any position
    count_1 = text.count(pattern)
    count_1 += count_pattern_0 * len(pattern)

    # Return the maximum count
    return max(count_0, count_1)


# Exercise-1
input_text_1 = "ababc"
input_pattern_1 = "ab"
output_1 = maximize_subsequences(input_text_1, input_pattern_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_text_2 = "ababab"
input_pattern_2 = "ab"
output_2 = maximize_subsequences(input_text_2, input_pattern_2)
print(f"Exercise-2 Output: {output_2}")
