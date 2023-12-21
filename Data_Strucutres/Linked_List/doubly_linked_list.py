class LinkedList[T]:
    class Node:
        def __init__(self, val: T, next=None, prev = None):
            self.val: T = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, val: T) -> None:
        newNode = self.Node(val)
        self.length += 1
        if not self.__bool__():
            self.head = newNode
            self.tail = newNode
            return
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def prepend(self, val: T) -> None:
        if not self.__bool__():
            return self.append(val)
        newNode = self.Node(val)
        self.length += 1
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def insertAt(self, val: T, index: int) -> None:
        if index > self.length:
            raise IndexError("Index out of bounds")
        elif index == self.length:
            self.prepend(val)
        elif index <= self.length // 2:
            curr = self.head
            while curr.next and index > 1:
                curr = curr.next
                index -= 1
            newNode = self.Node(val, curr.next, curr)
            curr.next.prev = newNode
            curr.next = newNode
        else:
            curr = self.tail
            i = self.length
            while curr.prev and i > index:
                curr = curr.prev
                i -= 1
            newNode = self.Node(val, curr.next, curr)
            curr.next.prev = newNode
            curr.next = newNode

    def remove(self, val: T) -> bool:
        """
        Tries to remove the first instance of val in the list.
        If the value is found, it is removed from the list and this returns True.
        If the value is not found, the list is unchanged and this returns False.
        """
        curr = self.head
        while curr:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return True
            curr = curr.next
        return False

    def removeAt(self, index: int) -> None:
        if index > self.length:
            raise IndexError("Index out of bounds")
        elif index == 0:
            self.head = self.head.next
            return
        elif index == self.length - 1:
            self.tail.prev.next = None
            return
        elif index <= self.length // 2:
            curr = self.head
            while curr and index > 0:
                curr = curr.next
                index -= 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            curr = self.tail
            i = self.length
            while curr.prev and i > (index + 1):
                curr = curr.prev
                i -= 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def __bool__(self) -> bool:
        return bool(self.head)
    
    def __str__(self) -> str:
        if not self.__bool__():
            return "[]"
        curr = self.head
        s = ""
        while curr and curr.next:
            s += str(curr.val) + " -> "
            curr = curr.next
        return "[" + s + str(curr.val) + "]"
    
    def __len__(self) -> int:
        return self.length