class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full. No room to insert")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):   # constat-time O(1)
        if (self.is_empty()):
            raise ValueError("No viable data to return, the queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None   # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.queue1 = Queue(10)
        self.queue1.put(1)
        self.queue1.put(2)
        self.queue1.put(3)
        self.queue1.put(4)
        self.queue2 = Queue(10)
    
    def test_is_empty(self):
        self.assertFalse(self.queue1.is_empty(), False)
        self.assertTrue(self.queue2.is_empty(), True)

    def test_is_full(self):
        self.assertFalse(self.queue1.is_full(), False)
        self.assertFalse(self.queue2.is_full(), False)         
    
    def test_put(self):
        self.queue2.put(6)
        self.assertEqual(self.queue2.is_empty(), False )

    def test_get(self):
        self.queue2.put(9)
        self.queue2.put(10)
        self.queue2.put(11)
        self.queue2.put(12)
        self.assertEqual(self.queue2.get(), 9)

        
if __name__ == '__main__':
    unittest.main()