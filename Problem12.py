#题目：判断101-200之间有多少个素数，并输出所有素数。
import math

number_prime = 0
for i in range(101,201):
	list_factors = []
	for j in range(2,math.ceil(math.sqrt(i)) + 1):
		if i % j == 0:
			list_factors.append(j)
			list_factors.append(int(i/j))
	if len(list_factors) > 0:
		number_prime = number_prime + 1
		print(i)

print("素数的个数是: ",number_prime)

