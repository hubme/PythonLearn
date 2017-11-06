import sys
sys.path.append("E:\Python\PythonLearn\mymodule")
from my_math import divide
import unittest

class DivideTestCase(unittest.TestCase):
	def testDivide1(self):	#以 test 开头的方法才会运行
		result = divide(4, 2)
		self.assertEqual(result, 2)

	def testDivide2(self):
		result = divide(4, 2)
		self.assertEqual(result, 3)

unittest.main()