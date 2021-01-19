import unittest
from day13.Jsq.cala import Calculator
class TestCalc1(unittest.TestCase):
    def testSub(self):
        c = Calculator()
        a = 9
        b = 10
        s = -1  # 期望结果
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub1(self):
        c = Calculator()
        a = -9
        b = -10
        s = 1  # 期望结果
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub2(self):
        c = Calculator()
        a = -9
        b = 10
        s = -19  # 期望结果
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub3(self):
        c = Calculator()
        a = 9
        b = -10
        s = 19  # 期望结果
        sum = c.sub(a, b)
        self.assertEquals(s, sum)