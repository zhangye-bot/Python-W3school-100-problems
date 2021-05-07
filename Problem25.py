#题目：求1+2!+3!+...+20!的和。


def sum_factorial(number):
	sum = 0 
	for i in range(1,number + 1):
		sum = sum + factorial(i)
	return sum


def factorial(number):
	result = 1
	for i in range(1,number + 1):
		result = result * i
	return result





sum = sum_factorial(20)
print(sum)












