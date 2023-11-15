def min_time_to_complete_tasks(tasks, workers):
    left, right = max(tasks), sum(tasks)

    def is_valid(mid):
        count_workers = 1
        curr_time = 0

        for task in tasks:
            curr_time += task
            if curr_time > mid:
                curr_time = task
                count_workers += 1

        return count_workers <= workers

    while left < right:
        mid = (left + right) // 2

        if is_valid(mid):
            right = mid
        else:
            left = mid + 1

    return left


# Exercise-1
input_tasks_1 = [10, 20, 30, 40]
input_workers_1 = 2
output_1 = min_time_to_complete_tasks(input_tasks_1, input_workers_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_tasks_2 = [60, 20, 40, 50]
input_workers_2 = 2
output_2 = min_time_to_complete_tasks(input_tasks_2, input_workers_2)
print(f"Exercise-2 Output: {output_2}")
