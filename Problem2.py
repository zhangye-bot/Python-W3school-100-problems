"""题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
							利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
							20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
							60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？"""


arr = [0,100000,200000,400000,600000,1000000]
rate = [0.1,0.075,0.05,0.03,0.015,0.01]
def bonus_calculator(profit):
	index = 0
	for i in range(0,6,1):
		if profit > arr[i]:
			index = index + 1


			# 8 index = 1 arr[0], 0.1  rate[0]
			# 11 index = 2 arr[1], 0.1 rate[1]
			# 21 index = 3 arr[2]. 0.1 rate[2]

	bonus = arr[index-1]*0.1+(profit-arr[index-1])*rate[index-1]
	print('您的当月奖金是%.2f'%bonus)




profit = float(input("请输入您的当月利润: "))
bonus_calculator(profit)
