class RingBuffer:
    # queue structure implemented using a python list
    # oldest item leaves queue first (FIFO) when capacity is reached, and new item is inserted to the end of the queue
    def __init__(self, capacity):
        self.capacity = capacity
        # works as a queue # has to initiate an array filled with None with size Capacity , otherwise index method will not work
        self.storage = [None]*capacity
        self.current_index = 0

    def append(self, item):
        self.storage[self.current_index] = item
        self.current_index += 1
        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self):
        filtered = [item for item in self.storage if item is not None]
        return filtered
