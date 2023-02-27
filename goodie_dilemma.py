def program(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)


    earnings = []
    last_job_end_time = 0
    for job in jobs:
        if job[0] >= last_job_end_time:
            earnings.append(job[2])
            last_job_end_time = job[1]


    num_jobs_left = len(jobs) - len(earnings)
    other_earnings = sum(job[2] for job in jobs if job[2] not in earnings)
    return (num_jobs_left, other_earnings)



n = int(input("Enter the number of Jobs\n"))
jobs = []
for i in range(n):
    start_time = int(input("Enter job start time\n"))
    end_time = int(input("Enter job end time\n"))
    profit = int(input("Enter job profit\n"))
    jobs.append((start_time, end_time, profit))


num_jobs_left, other_earnings = program(jobs)

# print the output
print("The number of tasks and earnings available for others")
print("Task:", num_jobs_left)
print("Earnings:", other_earnings)
