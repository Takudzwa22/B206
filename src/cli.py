from process import Process
from scheduler import fcfs, sjf, round_robin
from memory_manager import MemoryManager

def run_cli():
    n = int(input("Number of processes: "))
    processes = []
    for i in range(n):
        pid = i + 1
        at = int(input(f"Arrival time for P{pid}: "))
        bt = int(input(f"Burst time for P{pid}: "))
        mem = int(input(f"Memory needed for P{pid}: "))
        processes.append(Process(pid, at, bt, mem))

    mem_size = int(input("Total memory size: "))
    memory = MemoryManager(mem_size)

    print("Choose Scheduling: 1.FCFS 2.SJF 3.Round Robin")
    choice = int(input("> "))
    if choice == 1:
        schedule = fcfs(processes)
    elif choice == 2:
        schedule = sjf(processes)
    else:
        q = int(input("Quantum: "))
        schedule = round_robin(processes, q)

    print("\nExecution Order:")
    for p in schedule:
        print(f"P{p.pid}: Start {p.start_time}, End {p.completion_time}")

if __name__ == "__main__":
    run_cli()
