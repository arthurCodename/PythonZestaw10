import random as rand

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def insert(self, data):
        if self.is_full():
            raise ValueError("Queue is full. No room to insert")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if (self.is_empty()):
            raise ValueError("No viable data to return, the queue is empty")
        index = rand.randint(0, self.tail - 1)
        node = self.items[index]
        self.items[index] = self.items[self.tail - 1]
        self.tail = self.tail -1 
        return node

    def clear(self):
        self.head = None
        self.tail= None
        self.n = 0


import unittest

class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.queue1 = RandomQueue(10)
        self.queue1.insert(1)
        self.queue1.insert(2)
        self.queue1.insert(3)
        self.queue1.insert(4)
        self.queue2 = RandomQueue(10)

    def test_insert(self):
        self.queue2.insert(6)
        self.assertEqual(self.queue2.is_empty(), False )

    def test_remove(self):
        self.queue2.insert(6)
        self.assertEqual(self.queue2.remove(), 6 )
        self.assertEqual(self.queue2.is_empty(), True)
     
    def test_is_empty(self):
        self.assertFalse(self.queue1.is_empty(), False)
        self.assertTrue(self.queue2.is_empty(), True)

    def test_is_full(self):
        self.assertFalse(self.queue1.is_full(), False)
        self.assertFalse(self.queue2.is_full(), False) 

    def test_clear(self):
        self.queue1.clear()
        self.assertEqual(self.queue1.head, None)
        self.assertEqual(self.queue1.tail, None)
        self.assertEqual(self.queue1.n, 0)

if __name__ == '__main__':
    unittest.main()  