"""题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。"""




def Is_Huiwen(number):
	digit_5 = number//10000 
	digit_4 = (number-digit_5*10000)//1000
	digit_3 = (number-digit_5*10000-digit_4*1000)//100
	digit_2 = (number-digit_5*10000-digit_4*1000-digit_3*100)//10
	digit_1 = (number-digit_5*10000-digit_4*1000-digit_3*100-digit_2*10)

	if digit_5 == digit_1 & digit_4 == digit_2:
		print("这个数字是回文数")
	else:
		print('这个数字不是回文数')

Is_Huiwen(12321)


