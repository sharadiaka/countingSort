import unittest
from countingSort import counting

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(counting(9,[1,5,7,8,2,9]), [1, 2, 5, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
