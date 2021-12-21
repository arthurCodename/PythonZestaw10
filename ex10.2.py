class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size
    
    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if(self.is_full()):
            raise ValueError("The stack is full. No room to push")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if (self.is_empty() == True):
            raise ValueError("The stack is empty. There's nothing to pop")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data




import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack()
        self.stack1.push(1)
        self.stack1.push(2)
        self.stack1.push(3)
        self.stack1.push(4)
        self.stack1.push(5)
        self.stack2 = Stack()
    
    def test_is_empty(self):
        self.assertFalse(self.stack1.is_empty(), False)
        self.assertTrue(self.stack2.is_empty(), True)

    def test_is_full(self):
        self.assertFalse(self.stack1.is_full(), False)
        self.assertFalse(self.stack2.is_full(), False)         
    
    def test_push(self):
        self.stack2.push(6)
        self.assertEqual(self.stack2.is_empty(), False )

    def test_pop(self):
        self.assertEqual(self.stack1.pop(), 5)

        
if __name__ == '__main__':
    unittest.main()