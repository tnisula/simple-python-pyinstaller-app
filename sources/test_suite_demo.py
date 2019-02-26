import unittest
from sources.test_class1 import test_class1
from sources.test_class2 import test_class2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(test_class1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_class2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)