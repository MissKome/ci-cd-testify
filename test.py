
# import main
# import unittest

# class TestMain(unittest.TestCase):

#      def test_addition(self):
#         self.assertEqual(main.addition(1,2), 3 ,"Should be 3")
#         self.assertEqual(main.addition(5,5), 10 ,"Should be 10")
#         self.assertEqual(main.addition(40,20), 60 ,"Should be 60")
#         self.assertEqual(main.addition(-3,2), -1 ,"Should be -1")

# if __name__ == "__main__":
#     unittest.main()

import main
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)

if __name__ == '__main__':
        unittest.main()

