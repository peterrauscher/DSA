class LinkedList[T]:
    class Node:
        def __init__(self, val: T, next=None):
            self.val: T = val
            self.next = next

    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, val: T) -> None:
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
            self.length += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def prepend(self, val: T) -> None:
        self.head = self.Node(val, self.head)
        self.length += 1

    def insertAt(self, val: T, index: int) -> None:
        curr = self.head
        if index == 0:
            return self.prepend(val)
        elif index > self.length:
            raise IndexError("Index is out of bounds")
        elif index == self.length:
            return self.append(val)
        while curr and curr.next and index > 1:
            curr = curr.next
            index -= 1
        newNode = self.Node(val, curr.next)
        curr.next = newNode
        self.length += 1

    def remove(self, val: T) -> None:
        if self.head and self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr and curr.next and not curr.next.val == val:
            curr = curr.next
        if curr and curr.next and curr.next.val == val:
            curr.next = curr.next.next
        else:
            raise ValueError("Value not in list")

    def removeAt(self, index: int) -> None:
        if index >= self.length:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        curr = self.head
        while curr and curr.next and index > 1:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        self.length -= 1

    def get(self, index: int):
        if not self.head or index >= self.length:
            raise IndexError("Index out of bounds")
        curr = self.head
        while curr and curr.next and index > 0:
            curr = curr.next
            index -= 1
        return curr.val

    def __str__(self) -> str:
        curr = self.head
        s = "["
        while curr:
            s += f"{str(curr.val)}"
            if curr.next:
                s += ", "
            curr = curr.next
        return s + "]"

    def __len__(self) -> int:
        return self.length
