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
        return not self.__bool__()

    def __bool__(self) -> bool:
        return self.head is not None

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        if not self.head:
            return "[]"
        reversed = []
        curr = self.head
        while curr:
            reversed.append(str(curr.value))
            curr = curr.next
        reversed.reverse()
        return "[" + ", ".join(reversed) + "]"
