
import unittest
import calc

class test_class1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print("*-" * 30)
        print("Test Class 1 -> class level setUp")
        print("*-" * 30)

    def setUp(self):
        print("Test Class 1 -> setUp")

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def tearDown(self):
        print("Test Class 1 -> tearDown")

    @classmethod
    def tearDownClass(cls):
        print()
        print("*-" * 30)
        print("Test Class 1 -> class level tearDown")
        print("*-" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)