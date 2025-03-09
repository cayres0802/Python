import unittest

from mymodule import square, doubler
class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)
    
    def test_doubler(self):
        self.assertEqual(doubler(2), 4)
        
if __name__ == '__main__':
    unittest.main()