"""题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
80 = 2 * 2 * 2 * 2 * 5 
100 = 2 * 2 * 5 * 5 
102 = 2 * 51 
104 = 2 * 2 * 2 * 13 
105 = 3 * 5 * 7 
8 = 2 * 2 * 2 
118 = 59 * 2 
"""
import math

#获取一个数从2到number/2的全部质数集合
def prime_list(number):
	prime_list = []
	for i in range (2,math.ceil(number/2)+1):
		if Is_Prime(i) == True:
			prime_list.append(i)
	return(prime_list)

#判断一个数是否为质数
def Is_Prime(number):
	if number == 2: 
		return True
	else:
		factor_list = []
		for i in range(2,math.ceil(math.sqrt(number)+1)):
			if number % i == 0:
				if i not in factor_list:
					factor_list.append(i)
					factor_list.append(int(number/i))

	if len(factor_list) == 0:
		return True
	else:
		return False


#将一个正整数分解质因数


def factorize_number(number):
	if Is_Prime(number) == True:
		print('数字是质数')
	else:
		number_factors = []
		prime_list1 = prime_list(number)
		index = 0
		flag = True
		while index < len(prime_list1):			
			while flag == True:
				remainder = number % prime_list1[index]
				if remainder == 0:
					number_factors.append(prime_list1[index])
					number = number / prime_list1[index]
					if number == 1:
						break
				else:
					flag = False


			index = index + 1
			flag = True

		return number_factors

#显示结果
def show_result(number):
		print(number,end= ' ')
		print('=',end=' ')
		number_factors = factorize_number(number)
		i = 0
		while i < len(number_factors) - 1:
			print(number_factors[i],end= ' * ')
			i = i + 1
		print(number_factors[len(number_factors)-1])



show_result(100)
