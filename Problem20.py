"""题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无"""
import math

def total_distance(height,n):
	if n == 1:
		return height
	else:
		distance = 0
		for i in range(1,n):
			distance = distance + 2 * bounce_height(height,i)
		return distance + height



def bounce_height(height,n):
	
	return(100/math.pow(2,n))




print('第10次反弹高度是%.4f米'%bounce_height(100,10))
print('总高度:%.4f'%total_distance(100,10))