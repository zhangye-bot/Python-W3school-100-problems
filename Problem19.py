#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

import math

#返回因子之和
def sum_factors(number):
	list1 = [1]
	for i in range(2,math.ceil(math.sqrt(number))):
		if number%i == 0:
			list1.append(i)
			list1.append(number/i)
	return sum(list1)


number_list = []
for number in range(1,100000):
	if sum_factors(number) == number:
		number_list.append(number)
print(number_list)
