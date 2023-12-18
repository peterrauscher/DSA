class StackEmptyError(Exception):
    """Raised when attempting to read from an empty stack."""

    pass


class Stack:
    """
    A stack implemented using a Linked List.
    All operations can be performed in O(1), or constant time.
    Supports mixed data types.
    """

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.len = 0
        self.head = None

    def push(self, x):
        X = self.Node(x, self.head)
        self.len += 1
        self.head = X

    def pop(self):
        if self.head is None:
            raise StackEmptyError("Trying to pop from an empty stack")
        x = self.head.value
        self.head = self.head.next
        self.len -= 1
        return x

    def peek(self):
        if self.head is None:
            raise StackEmptyError("Trying to peek from an empty stack")
        return self.head.value

    def empty(self):
        return self.head is None

    def size(self):
        return self.len


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.pop())
    print(s.size())
    print(s.empty())
