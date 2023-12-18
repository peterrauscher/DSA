import unittest

from Data_Strucutres.queue_linked_list import Queue


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


if __name__ == "__main__":
    unittest.main()
