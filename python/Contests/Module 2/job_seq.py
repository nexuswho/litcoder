def job_sequencing(job_count, job_names, deadlines, profits):
    jobs = list(zip(job_names, deadlines, profits))
    jobs.sort(key=lambda x: x[2], reverse=True)

    result = [None] * job_count
    slot = [False] * (job_count + 1)

    for i in range(job_count):
        for j in range(min(job_count, jobs[i][1]), 0, -1):
            if not slot[j]:
                result[j - 1] = jobs[i][0]
                slot[j] = True
                break

    return [job for job in result if job is not None]


# Exercise-1
input_job_count_1 = 5
input_job_names_1 = ["a", "b", "c", "d", "e"]
input_deadlines_1 = [2, 1, 2, 1, 3]
input_profits_1 = [100, 19, 27, 25, 15]
output_1 = job_sequencing(
    input_job_count_1, input_job_names_1, input_deadlines_1, input_profits_1
)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_job_count_2 = 5
input_job_names_2 = ["p", "q", "r", "s", "t"]
input_deadlines_2 = [2, 1, 3, 1, 3]
input_profits_2 = [99, 190, 27, 25, 15]
output_2 = job_sequencing(
    input_job_count_2, input_job_names_2, input_deadlines_2, input_profits_2
)
print(f"Exercise-2 Output: {output_2}")
