import unittest
from area import calcula

class AreaTest(unittest.TestCase):
    def test_1_when_1(self):
        self.assertEqual(calcula(1), 1)

    def test_4_when_2(self):
        self.assertEqual(calcula(4), 2)

    def test_9_when_3(self):
        self.assertEqual(calcula(3), 3)
        
