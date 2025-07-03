class MemoryManager:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size

    def first_fit(self, process):
        needed = process.memory_required
        start = -1
        count = 0
        for i, slot in enumerate(self.memory):
            if slot is None:
                if count == 0:
                    start = i
                count += 1
                if count == needed:
                    for j in range(start, start + needed):
                        self.memory[j] = process.pid
                    return True
            else:
                count = 0
        return False

    def best_fit(self, process):
        best_start = -1
        best_size = float('inf')
        i = 0
        while i < self.size:
            if self.memory[i] is None:
                start = i
                while i < self.size and self.memory[i] is None:
                    i += 1
                length = i - start
                if process.memory_required <= length < best_size:
                    best_start = start
                    best_size = length
            i += 1
        if best_start != -1:
            for j in range(best_start, best_start + process.memory_required):
                self.memory[j] = process.pid
            return True
        return False
