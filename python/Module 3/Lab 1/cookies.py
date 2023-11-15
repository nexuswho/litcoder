import heapq


def candies_steps(target, candies):
    heapq.heapify(candies)  # Convert the candies list into a min-heap

    steps = 0
    while len(candies) > 1:
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)
        new_sweetness = least_sweet + 2 * second_least_sweet
        heapq.heappush(candies, new_sweetness)
        steps += 1

        if candies[0] >= target:
            break

    return steps


# Exercise-1
input_target_1 = 7
input_candies_1 = [1, 2, 3, 4, 5]
output_1 = candies_steps(input_target_1, input_candies_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_target_2 = 11
input_candies_2 = [2, 5, 3, 7, 6, 1]
output_2 = candies_steps(input_target_2, input_candies_2)
print(f"Exercise-2 Output: {output_2}")
