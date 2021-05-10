"""题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


请输入一个数:
23459
5 位数： 9 5 4 3 2
请输入一个数:
3472
4 位数： 2 7 4 3
"""
#number = int(input("请输入数字: "))
number = 4324
number_5 = number//10000
number_4 = (number-number_5*10000)//1000
number_3 = (number-number_5*10000-number_4*1000)//100
number_2 = (number-number_5*10000-number_4*1000-number_3*100)//10
number_1 = number-number_5*10000-number_4*1000-number_3*100-number_2*10

#判断是几位数,逆序打印出各位数字
if number_5 != 0:
	print("五位数")
	print(number_1,number_2,number_3,number_4,number_5)
elif number_4 != 0:
	print("四位数")
	print(number_1,number_2,number_3,number_4)
elif number_3 != 0:
	print('三位数')
	print(number_1,number_2,number_3)
elif number_2 != 0:
	print("俩位数")
	print(number_1,number_2)
else:
	print("一位数")
	print(number_1)


