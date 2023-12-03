import math

class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.count = 0

    def append(self, value):
        self.buffer[self.count % self.size] = value
        self.count += 1

    def get_average(self):
        if self.count == 0:
            return 0
        return sum(self.buffer) / min(self.count, self.size)

    def get_std_dev(self):
        if self.count == 0:
            return 0
        avg = self.get_average()
        variance = sum((x - avg) ** 2 for x in self.buffer) / min(self.count, self.size)
        return math.sqrt(variance)
