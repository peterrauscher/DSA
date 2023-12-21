class Queue[T]:
    class Node:
        def __init__(self, val : T, next = None, prev = None) -> None:
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, val: T):
        new_node = self.Node(val)
        self.length += 1
        if self.empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def dequeue(self) -> T:
        if self.empty():
            raise IndexError("Cannot deque from an empty queue")
        self.length -= 1
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def peek(self) -> T:
        if self.empty():
            raise IndexError("Cannot peek from an empty queue")
        return self.tail.val
    
    def empty(self) -> bool:
        return self.length == 0
    
    def __bool__(self) -> bool:
        return not self.empty()
    
    def __str__(self) -> str:
        if not bool(self):
            return "[]"
        s = ""
        curr = self.head
        while curr.next:
            s += str(curr.val) + " -> "
            curr = curr.next
        return "[" + s + str(curr.val) + "]"