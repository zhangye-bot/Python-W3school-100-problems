#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
number = 0
for i in range(1,5,1):
	for j in range(1,5,1):
		for k in range(1,5,1):
			if (i != j) & (j != k) & (i != k):
				number = number + 1
				print(i,j,k)

print('一共有%d个互不相同且无重复数字的三位数'%number)