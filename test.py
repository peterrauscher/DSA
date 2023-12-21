import random
import unittest

from Algorithms.Sort.bubble_sort import bubble_sort
from Data_Strucutres.Linked_List.doubly_linked_list import (
    LinkedList as DoublyLinkedList,
)
from Data_Strucutres.Linked_List.singly_linked_list import (
    LinkedList as SinglyLinkedList,
)
from Data_Strucutres.Queue.queue_linked_list import Queue

# from Data_Strucutres.Linked_List.doubly_linked_list import LinkedList as DoublyLinkedList


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(str(self.queue), "[1]")

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(str(self.queue), "[2]")

    def test_empty(self):
        self.assertTrue(self.queue.empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.empty())

    def test_str(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "[2, 1]")


class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        test_list = [random.randint(-1000, 1000) for _ in range(10**4)]
        self.assertEqual(sorted(test_list), bubble_sort(test_list))


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = DoublyLinkedList()

    def test_append(self):
        self.assertTrue(not bool(self.ll))
        for i in range(10):
            self.ll.append(i)
        self.assertEqual(
            str(self.ll), "[" + " -> ".join([str(i) for i in range(10)]) + "]"
        )

    def test_remove(self):
        self.assertTrue(not bool(self.ll))
        for i in range(10):
            self.ll.append(i)
        self.assertEqual(
            str(self.ll), "[" + " -> ".join([str(i) for i in range(10)]) + "]"
        )
        self.ll.remove(8)
        print(self.ll)
        self.assertEqual(
            str(self.ll),
            "[" + " -> ".join([str(i) for i in range(10) if i != 8]) + "]",
        )

    def test_remove_at(self):
        self.assertTrue(not bool(self.ll))
        for i in range(10):
            self.ll.append(i)
        self.assertEqual(
            str(self.ll), "[" + " -> ".join([str(i) for i in range(10)]) + "]"
        )
        self.ll.removeAt(5)
        self.ll.removeAt(5)
        self.assertEqual(
            str(self.ll),
            "[" + " -> ".join([str(i) for i in range(10) if i != 5 and i != 6]) + "]",
        )


if __name__ == "__main__":
    unittest.main()
