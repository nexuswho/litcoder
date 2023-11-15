def longest_substring_without_repeating(s):
    char_index_map = {}  # To store the index of each character
    start_index = 0  # Starting index of the current substring
    max_length = 0  # Maximum length of substring without repeating characters

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start_index:
            # If the character is repeated and its previous occurrence is within the current substring
            start_index = char_index_map[char] + 1

        char_index_map[char] = i  # Update the index of the character
        current_length = i - start_index + 1

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, current_length)

    return max_length


# Exercise-1
input_str_1 = "pqrsstu"
output_1 = longest_substring_without_repeating(input_str_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_str_2 = "abbedfgi"
output_2 = longest_substring_without_repeating(input_str_2)
print(f"Exercise-2 Output: {output_2}")
