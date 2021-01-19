import unittest
from day13.Jsq.cala import Calculator
class TestCalc2(unittest.TestCase):
    def testDiv(self):
        c = Calculator()
        a = 9
        b = 10
        s = 0.9  # 期望结果
        sum = c.div(a, b)
        self.assertEquals(s, sum)

    def testDiv1(self):
        c = Calculator()
        a = -9
        b = -10
        s = 0.9  # 期望结果
        sum = c.div(a, b)
        self.assertEquals(s, sum)

    def testDiv2(self):
        c = Calculator()
        a = 9
        b = -10
        s = -0.9  # 期望结果
        sum = c.div(a, b)
        self.assertEquals(s, sum)

    def testDiv3(self):
        c = Calculator()
        a = -9
        b = 10
        s = -0.9  # 期望结果
        sum = c.div(a, b)
        self.assertEquals(s, sum)
