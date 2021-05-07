#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

import math

#返回因子之和
def sum_factors(number):
	list1 = []
	for i in range(1,math.ceil(number/2)+1):
		if number%i == 0:
			list1.append(i)
	return sum(list1)


number_list = []
for number in range(1,1001):
	if sum_factors(number) == number:
		number_list.append(number)
print(number_list)
