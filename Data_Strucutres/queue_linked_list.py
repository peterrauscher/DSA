class Queue[T]:
    class Node:
        def __init__(self, val : T, next = None, prev = None) -> None:
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val: T):
        new_node = self.Node(val)
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
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def peek(self) -> T:
        if self.empty():
            raise IndexError("Cannot peek from an empty queue")
        return self.tail.val
    
    def empty(self) -> bool:
        return not self.head
    
    def __bool__(self) -> bool:
        return self.empty()
    
    def __str__(self) -> str:
        s = "["
        curr = self.head
        while curr:
            s += str(curr.val)
            if curr.next:
                s += ", "
            curr = curr.next
        return s + "]"