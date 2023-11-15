def find_peaks(heights):
    try:
        peaks_count = 0
        highest_peaks = []

        for i in range(1, len(heights) - 1):
            if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
                peaks_count += 1
                highest_peaks.append(heights[i])

        return peaks_count, highest_peaks

    except (ValueError, TypeError):
        return "Input was not in a correct format"


# Exercise-1
heights_1 = [1, 3, 5, 4, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
output_1 = find_peaks(heights_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
heights_2 = [5, 4, 3, 2, 1, 2, 3, 4, 5]
output_2 = find_peaks(heights_2)
print(f"Exercise-2 Output: {output_2}")

# Exercise-3
heights_3 = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
output_3 = find_peaks(heights_3)
print(f"Exercise-3 Output: {output_3}")

# Exercise-4
heights_4 = [1, 2, "a"]
output_4 = find_peaks(heights_4)
print(f"Exercise-4 Output: {output_4}")
