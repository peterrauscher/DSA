class Stack:
    """
    Stack implemented with a list/dynamic array as the backing store.
    Inefficient, operations take O(n-1) or simply O(n).
    Supports mixed data types (thanks python).
    """

    def __init__(self):
        self.data = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def size(self) -> int:
        return len(self.data)

    def peek(self):
        return self.data[-1]

    def pop(self):
        e = self.data[-1]
        self.data = self.data[:-1]
        return e

    def push(self, x):
        self.data.append(x)


if __name__ == "__main__":
    s = Stack()
    print(s.empty())
    print(s.size())
    s.push(2)
    s.push(14)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.size())
    s.push(23)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.empty())
