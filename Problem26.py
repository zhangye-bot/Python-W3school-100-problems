#题目：利用递归方法求5!。


def factorial(number):
	if number == 0:
		result = 1
	else:
		result = number * factorial(number-1)
	return result


print(factorial(4))
