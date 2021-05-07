"""题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。"""
from fractions import Fraction

number = int(input("请输入您想计算的数列个数: "))

numerators = []
numerators.append(2)
numerators.append(3)
for i in range(2,number,1):
	numerator = numerators[i-1] + numerators[i-2]
	numerators.append(numerator)


denumerators = []
denumerators.append(1)
denumerators.append(2)
for i in range(2,number,1):
	denumerator = denumerators[i-1] + denumerators[i-2]
	denumerators.append(denumerator)

numbers = []
for i in range(0,len(numerators)):
	numbers.append(Fraction(numerators[i],denumerators[i]))

print("前%d项之和是%.2f"%(number,sum(numbers)))
