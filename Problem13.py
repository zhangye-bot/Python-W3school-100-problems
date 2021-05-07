"""题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。"""
import math
for number in range(100,1000):
	number_hundred = number//100
	number_ten = (number-number_hundred * 100)//10
	number_one = number - number_ten * 10 - number_hundred * 100

	if number == (pow(number_hundred,3) + pow(number_ten,3) + pow(number_one,3)):
		print(number)
	