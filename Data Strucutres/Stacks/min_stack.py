class MinStack:
    class Node:
        def __init__(self, val, next=None):
            self.next = next
            self.val = val

    def __init__(self):
        self.head = None
        self.minHead = None
        self.size = 0

    def push(self, val: int) -> None:
        if self.minHead is None or val <= self.minHead.val:
            self.minHead = self.Node(val, self.minHead)
        self.head = self.Node(val, self.head)
        self.size += 1

    def pop(self):
        if self.head.val == self.minHead.val:
            self.minHead = self.minHead.next
        v = self.head.val
        self.head = self.head.next
        self.size -= 1
        return v

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.minHead.val
