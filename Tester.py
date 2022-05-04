import unittest
from main import verify


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(verify("x+2", '0', '2'), 1)

    def test2(self):
        self.assertEqual(verify("x^2+5", '-5', '5'), 1)

    def test3(self):
        self.assertEqual(verify("3*x^2", '5', '-5'), 0)

    def test4(self):
        self.assertEqual(verify("x^2+5", "a", '5'), 0)

    def test5(self):
        self.assertEqual(verify("3*x", '-5', ""), 0)

    def test6(self):
        self.assertEqual(verify("t^2+5", '-5', '5'), 0)

    def test7(self):
        self.assertEqual(verify("", '-5', '5'), 0)

    def test8(self):
        self.assertEqual(verify("Ahmed", '-5', '5'), 0)


if __name__ == '__main__':
    unittest.main()
