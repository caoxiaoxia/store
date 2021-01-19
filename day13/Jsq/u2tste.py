import unittest
from day13.Jsq.cala import Calculator
class TestCalc2(unittest.TestCase):
    def testMul(self):
        c = Calculator()
        a = 9
        b = 10
        s = 90  # 期望结果
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul1(self):
        c = Calculator()
        a = -9
        b = -10
        s = 90  # 期望结果
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul2(self):
        c = Calculator()
        a = -9
        b = 10
        s = -90  # 期望结果
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul3(self):
        c = Calculator()
        a = 9
        b = -10
        s = -90  # 期望结果
        sum = c.mul(a, b)
        self.assertEquals(s, sum)