import unittest
from day13.Jsq.cala import Calculator
class TestCalc(unittest.TestCase):
    def testAdd(self):
        c = Calculator()
        a = 9
        b = 10
        s = 19      #期望结果
        sum = c.add(a,b)   #实际结果
        self.assertEquals(s,sum)

    def testAdd1(self):
        c = Calculator()
        a = -9
        b = -10
        s = -19  # 期望结果
        sum = c.add(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testAdd2(self):
        c = Calculator()
        a = 9
        b = -10
        s = -1  # 期望结果
        sum = c.add(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testAdd3(self):
        c = Calculator()
        a = -9
        b = 10
        s = 1  # 期望结果
        sum = c.add(a, b)  # 实际结果
        self.assertEquals(s, sum)
