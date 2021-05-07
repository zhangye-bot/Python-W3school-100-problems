#题目：求100之内的素数。
import math

list_primes = [2]
for i in range(3,10000):
	list_factors = []
	for j in range(2,math.ceil(math.sqrt(i))+1):
		if i%j == 0:
			list_factors.append(j)
			if j != math.sqrt(i):
				list_factors.append(int(i/j))
	if len(list_factors) == 0:
		list_primes.append(i)

print(list_primes)

