import unittest
import os
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite() # 获取一个测试集

# 使用测试加载器: 使用默认加载器，去寻找（"用例所在路径","测试用例名称的规则"）   os.getcwd()获取当前文件的所在绝对路径
tests = unittest.defaultTestLoader.discover(os.getcwd(),"*tste.py")
suite.addTest(tests)

# 创建一个文本的运行器：产生的结果会以文本方式展示
# runner = unittest.TextTestRunner()
# 使用html运行器：生成以html结果报告
f = open("计算器的测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(     # 使用html运行器写入到报告里
    stream = f,     # 将报告写到那个文件流
    verbosity = 1,      # 报告的详细程度
    title = "计算器的测试报告"
)

# 使用运行器来运行测试集
runner.run(suite)
