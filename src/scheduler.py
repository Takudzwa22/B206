def fcfs(processes):
    time = 0
    schedule = []
    for p in sorted(processes, key=lambda x: x.arrival_time):
        start = max(time, p.arrival_time)
        p.start_time = start
        p.completion_time = start + p.burst_time
        time = p.completion_time
        schedule.append(p)
    return schedule

def sjf(processes):
    time = 0
    schedule = []
    ready_queue = []
    processes = sorted(processes, key=lambda x: x.arrival_time)
    while processes or ready_queue:
        while processes and processes[0].arrival_time <= time:
            ready_queue.append(processes.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda x: x.burst_time)
            p = ready_queue.pop(0)
            p.start_time = time
            p.completion_time = time + p.burst_time
            time = p.completion_time
            schedule.append(p)
        else:
            time += 1
    return schedule

def round_robin(processes, quantum=4):
    from collections import deque
    time = 0
    queue = deque(sorted(processes, key=lambda x: x.arrival_time))
    schedule = []
    while queue:
        p = queue.popleft()
        if p.remaining_time > quantum:
            p.remaining_time -= quantum
            time += quantum
            queue.append(p)
        else:
            time += p.remaining_time
            p.remaining_time = 0
            p.completion_time = time
            schedule.append(p)
    return schedule
