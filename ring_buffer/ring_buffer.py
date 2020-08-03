class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.data = self.data + [item]

    def get(self):
        return self.data
