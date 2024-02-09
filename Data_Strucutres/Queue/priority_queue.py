class PriorityQueue[T]:
    def __init__(self) -> None:
        self.priorities = {}
        self.highest = -1

    def enqueue(self, val, pty) -> None:
        if pty > self.highest:
            self.highest = pty
        
        
    def dequeue(self) -> T:

    def peek(self) -> T:
        if self.empty():
            raise IndexError("Cannot peek from an empty queue")
        return self.tail.val