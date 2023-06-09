
import main
import unittest

class TestMain(unittest.TestCase):

     def test_addition(self):
        self.assertEqual(main.addition(1,2), 3 ,"Should be 3")
        self.assertEqual(main.addition(5,5), 10 ,"Should be 10")
        self.assertEqual(main.addition(40,20), 60 ,"Should be 60")
        self.assertEqual(main.addition(-3,2), -1 ,"Should be -1")

     def test_subtraction(self):
        self.assertEqual(main.subtraction(5, 2), 3, "Should be 3")
        self.assertEqual(main.subtraction(7, 2), 5, "Should be 3")
        self.assertEqual(main.subtraction(9, 7), 2, "Should be 3")
        # self.assertEqual(main.subtraction(10, 7), 3, "Should be 3")

if __name__ == "__main__":
    unittest.main()

